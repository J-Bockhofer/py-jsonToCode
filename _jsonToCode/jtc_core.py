from templating.codeblock import CodeBlock

import json
import os

def decode_layer(data:dict, classname:str='', layerdepth:int=0) -> list[CodeBlock]:
    
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

    keynum = 0
    inithead = f'def __init__(self'
    for key in data:
        
        val = data[key]
        valtype = type(val)
        typestr = valtype.__name__ 
        todict_body_str = f'"{key}": self.{key}, '
        from_dict_body_ifbody_returnstr_tmp = f'data["{key}"], '
        from_dict_body_elsebody_tmp = f'{classname}'
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

def json_to_code(jsonfilename:str, codefilename:str) -> str:
    if os.path.exists(jsonfilename):
        with open(jsonfilename, "r", encoding='utf-8-sig') as data_file:
            data = json.load(data_file)  

    code = dict_to_code(data, codefilename)
    return code

def generate_test(jsonfilename:str, codefilename:str):
    # take code, generate test
    #os.path.dirname(os.path.abspath())
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
    testopenhead = f'with open("{jsonfilename}", "r", encoding="utf-8-sig") as data_file'
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

    with open(testfile, 'w') as f:
        f.write(importhead + testcode.__str__() + dundermain.__str__())
    
def rename_classes(codefile:str):
    if os.path.exists(codefile):
        with open(codefile, "w") as data_file:
            lines = data_file.readlines()

        # in lines find every class definition and its name
        # list properties

    
    