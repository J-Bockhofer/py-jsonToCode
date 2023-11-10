from templating.codeblock import CodeBlock

import json
import os

import re

def decode_layer(data:dict, classname:str='', layerdepth:int=0) -> list[CodeBlock]:
    """
        Function decodes the current dictionary, recursively decodes any contained dictionaries \n
        Generates code for classes with \n
        __init__() \n
        to_dict() \n
        from_dict() \n
    """
    if classname == '':
        classname += f'L_{layerdepth}'

    classhead = f'class {classname}'

    initblock = []
    codeblocks = []

    todict_head = f'def to_dict(self)->dict'
    todict_body = 'return {'

    from_dict_head = f'def from_dict(cls, data:dict)'
    from_dict_body_if = 'if ' # if object property1 in data and object property2 in data 
    from_dict_body_if_lists = []
    from_dict_body_ifbody_returnstr = 'return cls('
    from_dict_body_else = 'else'
    from_dict_body_elsebody = 'raise KeyError("Invalid data for '
    from_dict_body_elsebody_tmp = f'{classname}'

    keynum = 0
    inithead = f'def __init__(self'
    for key in data:
        
        val = data[key]
        valtype = type(val)
        typestr = valtype.__name__ 
        todict_body_str = f'"{key}": self.{key}, '
        from_dict_body_ifbody_returnstr_tmp = f'data["{key}"], '
        
        # if its a list check what the element types are to make it typesafe 
        # and identify nexted dicts, need to check if dicts are same
        if valtype == type([]):
            elementtypelist = []
            lastdict = {}
            dictnum = 0
            uniquedicts = 0

            for element in val:
                elementtype = type(element)
                if elementtype == type({}):
                    dictnum += 1
                    # check the dict
                    
                    if lastdict:
                        if lastdict.keys() != element.keys(): # if dicts are not the same
                            classstr = f'L_{layerdepth}_{keynum}_{dictnum}'
                            nthclassblocklist = decode_layer(element, classname=classstr, layerdepth=layerdepth+1)
                            codeblocks += nthclassblocklist
                            uniquedicts += 1

                    else:
                        classstr = f'L_{layerdepth}_{keynum}_{dictnum}'
                        lastdict = element
                        uniquedicts += 1
                        nthclassblocklist = decode_layer(element, classname=classstr, layerdepth=layerdepth+1)
                        codeblocks += nthclassblocklist
                        addlisttype = f'[{classstr}]'
                        
                elementtypelist.append(elementtype)

            typeset = set(elementtypelist)

            if len(typeset) == 1:
                # homogenous list

                if elementtype == type({}):
                    if uniquedicts == 1:
                        typestr += addlisttype
                        from_dict_body_if_lists.append(f'classlist_{key} = [{classstr}.from_dict(classdata) for classdata in data.get("{key}", [])]') 
                        from_dict_body_ifbody_returnstr_tmp = f'classlist_{key}, '
                        from_dict_body_elsebody_tmp = f'{classname}'
                        
                    else:
                        typestr += f'[{elementtype.__name__}]'
                        from_dict_body_if_lists.append(f'classlist_{key} = data["{key}"]')
                        from_dict_body_ifbody_returnstr_tmp = f'classlist_{key}, '
                    todict_body_str = f'"{key}": [x.to_dict() for x in self.{key}], '

                else:
                    typestr += f'[{elementtype.__name__}]'
                    todict_body_str = f'"{key}": self.{key}, '

            # gets tricky here, heterogenous list -> unsolved

        # if theres a dict decode that dict with layerdepth + 1
        if valtype == type({}):
            typestr = f'L_{layerdepth}_{keynum}'
            nthclassblocklist = decode_layer(val, classname=typestr, layerdepth=layerdepth+1)
            codeblocks += nthclassblocklist
            todict_body_str = f'"{key}": self.{key}.to_dict(), '
            from_dict_body_ifbody_returnstr_tmp = f'{typestr}.from_dict(data["{key}"]), '
   
        inithead += f', {key}:{typestr}'
        
        todict_body += todict_body_str
        blockstr = f'self.{key} = {key}'
        initblock.append(blockstr)

        from_dict_body_if += f'"{key}" in data and '
        #                                    ^12345^ 
        # delete these 5 chars after last iteration
        from_dict_body_ifbody_returnstr += from_dict_body_ifbody_returnstr_tmp

        keynum += 1
    inithead += f')'
    todict_body = todict_body[:-1]
    todict_body = todict_body[:-1]
    from_dict_body_if = from_dict_body_if[:-5]
    from_dict_body_ifbody_returnstr = from_dict_body_ifbody_returnstr[:-2]
    from_dict_body_ifbody_returnstr += ')'
    from_dict_body_elsebody += from_dict_body_elsebody_tmp + '")'

    todict_body += '}'

    initcodepy = CodeBlock(inithead, initblock)
    todict_code = CodeBlock(todict_head, [todict_body])
    fromdict_code_if = CodeBlock(from_dict_body_if, from_dict_body_if_lists + [from_dict_body_ifbody_returnstr])
    fromdict_code_else = CodeBlock(from_dict_body_else, [from_dict_body_elsebody])
    fromdict_code = CodeBlock(from_dict_head, [fromdict_code_if, fromdict_code_else])
    classcodeblock = CodeBlock(classhead, [initcodepy, todict_code, '@classmethod', fromdict_code])
    codeblocks.append(classcodeblock)
    return codeblocks

def dict_to_code(data:dict, filename:str) -> str:
    result = decode_layer(data)
    fulltxt = ''
    for res in result:
        fulltxt += res.__str__()

        with open(filename, 'w') as f:
            f.write(fulltxt)
    return fulltxt

def json_to_code(jsonfilename:str, codefilename:str, encoding:str='utf-8-sig') -> str:
    if os.path.exists(jsonfilename):
        with open(jsonfilename, "r", encoding=encoding) as data_file:
            data = json.load(data_file)  

    code = dict_to_code(data, codefilename)
    return code

def generate_test(jsonfilename:str, codefilename:str, encoding:str='utf-8-sig') -> str:
    """
        takes code and json to generate a test \n
        tests equality of input json and serialized class.to_dict() output
    """
    path, file = os.path.split(os.path.abspath(codefilename))
    module = file.split('.')[0]
    testfile = path+'/test_'+file
    importhead = f'''\
import unittest
import json
from {module} import *

'''
    testcodehead = 'class TestSerializer(unittest.TestCase)'
    testfunchead = 'def test_serializer(self)'
    testopenhead = f'with open("{jsonfilename}", "r", encoding="{encoding}") as data_file'
    testopenbody = 'data = json.load(data_file)' 
    testopencode = CodeBlock(testopenhead, [testopenbody])
    testfuncbody = [testopencode,
                    'root = L_0.from_dict(data)',
                    'data_b = root.to_dict()',
                    'self.maxDiff = None',
                    'self.assertEqual(data, data_b)']
    
    testfunccode = CodeBlock(testfunchead, testfuncbody)

    testcode = CodeBlock(testcodehead, [testfunccode])

    dundermain = CodeBlock('if __name__ == "__main__"',['unittest.main()'])

    fulltxt = importhead + testcode.__str__() + dundermain.__str__()

    with open(testfile, 'w') as f:
        f.write(fulltxt)    
    return fulltxt, testfile
    
def rename_class(prevName:str, newName:str, text:str) ->str:
    text = text.replace(prevName, newName)
    return text

def write_to_file(text:str, file:str):
    with open(file, 'w') as f:
        f.write(text)

def text_from_file(file:str) -> str:
    with open(file, 'r') as f:
       text = f.read()
    return text

def find_classes(text:str) -> list[str]:
    class_names = re.findall(r'.*class (.+):', text)
    class_names.sort()
    return class_names

def find_inits_for_classes(text:str, class_names:list[str]) ->list[str]:
    inits = []
    for name in class_names:
        init = re.findall(r'.*class '+re.escape(name)+r':\n.*(def __init__\(.*\)):', text)[0]
        inits.append(init)
    return inits

def replace_root_test(testcode:str, newName:str, oldname:str='') -> str:
    root_name = re.findall(r'.*root = (.+).from_dict', testcode)[0]
    if oldname:
        if oldname == root_name:
            testcode = testcode.replace(root_name, newName)
    else:
        testcode = testcode.replace(root_name, newName)
    return testcode


        # in lines find every class definition and its name
        # list properties

    
    