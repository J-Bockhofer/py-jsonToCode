from templating.codeblock import CodeBlock
from templating.py_lang import py_keywords_conv
import templating.py_template as pyt
#from templating.py_template import make_init_block, make_todict_block, make_fromdict_block, make_eq_block

import json
import os

import re


def decode_layer(data:dict, classname:str='', layerdepth:int=0, randomizer:bool=True) -> list[CodeBlock]:
    """
        Function decodes the current dictionary, recursively decodes any contained dictionaries \n
        Generates code for classes with methods \n
        __init__() \n
        __eq__() \n
        __str__() \n
        to_dict() \n
        from_dict() \n

        \n
            
    """
    if classname == '':
        classname += f'L_{layerdepth}'

    classhead = f'class {classname}'

    safekeylist=[]
    typelist=[]
    inkeylist =[]
    uniquedictlist=[] 
    singledictlist = []

    classstrlist = []
    classstr = ''

    codeblocks = []

    keynum = 0

    for key in data:
        safe_key = to_safe_key(key)
        safekeylist.append(safe_key)
        inkeylist.append(key)

        val = data[key]
        valtype = type(val)
        typestr = valtype.__name__ 
        uniquedicts = 0
        validsingledict = 0 # 0 if not dict, 1 if valid class dict, 2 if invalid class dict
        
        # if its a list check what the element types are to make it typesafe 
        # and identify nexted dicts, need to check if dicts are same
        if valtype == type([]):
            elementtypelist = []
            lastdict = {}
            dictnum = 0
            #uniquedicts = 0
            addlisttype = None
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
                            
                            if nthclassblocklist:
                                #if len(lastdict.keys() - element.keys()) < len(lastdict.keys())/2:
                                    # last dict is similar enough to be same
                                    # who is bigger
                                    #if len(lastdict.keys())>len(element.keys()):
                                    #    addlisttype = f'[{lastdictcstr}, '
                                    #else:
                                    #    addlisttype = f'[{classstr}, '
                                    #pass
                                #else:
                                addlisttype += f'{classstr}, '
                                uniquedicts += 1
                            else:
                                addlisttype += f'dict, '
                                uniquedicts += 1
                            # need to check which properties are optional to remove them from strict checking and give them a default value
                            

                    else:
                        # this is the first dict discovered
                        classstr = f'L_{layerdepth}_{keynum}_{dictnum}'
                        lastdict = element
                        lastdictcstr = classstr
                        uniquedicts += 1
                        nthclassblocklist = decode_layer(element, classname=classstr, layerdepth=layerdepth+1)
                        codeblocks += nthclassblocklist
                        if nthclassblocklist:
                            addlisttype = f'[{classstr}, '
                        else:
                            addlisttype = f'[dict, '
                        
                elementtypelist.append(elementtype)
            if addlisttype:
                addlisttype = addlisttype[:-2]
                addlisttype += ']'

            typeset = set(elementtypelist)

            if len(typeset) == 1:
                # homogenous list

                if elementtype == type({}):
                    if uniquedicts == 1:
                        typestr += addlisttype            
                    else:
                        typestr += addlisttype
                else:
                    typestr += f'[{elementtype.__name__}]'

            # gets tricky here, heterogenous list -> potentially unsolved

        # if theres a dict decode that dict with layerdepth + 1
        if valtype == type({}):
            typestr = f'L_{layerdepth}_{keynum}'
            nthclassblocklist = decode_layer(val, classname=typestr, layerdepth=layerdepth+1)
            codeblocks += nthclassblocklist
            if nthclassblocklist:
                validsingledict = 1
            else:
                validsingledict = 2
                typestr = f'dict'               
   

        typelist.append(typestr)
        uniquedictlist.append(uniquedicts)
        singledictlist.append(validsingledict)
        classstrlist.append(classstr)

        keynum += 1


    init_block = pyt.make_init_block(safekeylist, typelist)
    eq_code = pyt.make_eq_block()
    str_code = pyt.make_str_block(classname, safekeylist, typelist)
    repr_code = pyt.make_repr_block(classname, safekeylist, typelist)
    todict_code = pyt.make_todict_block(inkeylist, safekeylist, typelist)
    fromdict_code = pyt.make_fromdict_block(classname, 
                                        inkeylist, 
                                        typelist, 
                                        uniquedictlist, 
                                        singledictlist, 
                                        classstrlist)
    fromrand_code = pyt.make_fromrandom_block(classname, safekeylist, typelist)
    docstring = pyt.make_doc_string(classname, init_block)

    classcodeblock = CodeBlock(classhead, [docstring, init_block, eq_code, str_code, repr_code, todict_code, '@classmethod', fromdict_code, '@classmethod', fromrand_code])
    if keynum > 0: # if dict wasnt empty
        codeblocks.append(classcodeblock)
    return codeblocks

def dict_to_code(data:dict, filename:str) -> str:
    result = decode_layer(data)
    importhead = f'''\
import random
import string

'''
    fulltxt = importhead
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
    testserdehead = 'def test_serializer(self)'
    testopenhead = f'with open("{jsonfilename}", "r", encoding="{encoding}") as data_file'
    testopenbody = 'data = json.load(data_file)' 
    testopencode = CodeBlock(testopenhead, [testopenbody])
    testserdebody = [testopencode,
                    'root = L_0.from_dict(data)',
                    'data_b = root.to_dict()',
                    'self.maxDiff = None',
                    'self.assertEqual(data, data_b)']
    testreprhead = 'def test_repr(self)'
    testreprbody = [testopencode,
                    'root = L_0.from_dict(data)',
                    'root_b = eval(repr(root))',
                    'self.maxDiff = None',
                    'self.assertEqual(root, root_b)']

    testrandhead = 'def test_rand(self)'
    testrandbody = ['root = L_0.from_random()',
                    'root_b = eval(repr(root))',
                    'self.maxDiff = None',
                    'self.assertEqual(root, root_b)']
    testserdecode = CodeBlock(testserdehead, testserdebody)

    testreprcode = CodeBlock(testreprhead, testreprbody)

    testrandcode = CodeBlock(testrandhead, testrandbody)

    testcode = CodeBlock(testcodehead, [testserdecode,'', testreprcode, '', testrandcode])

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
        init = re.findall(r'.*class '+re.escape(name)+r':[\s\S\w\W]*?(def __init__\(.*\)):', text)[0]
        inits.append(init)
    return inits

def find_class_contexts(classnames:list[str], inits:list[str])->dict:
    # only non-root class contexts, root is always classnames[0]
    classnames = classnames[1:]
    classcontext = {}
    for i in range(0,len(inits)):
        init = inits[i]
        # regex find properties with type
        # (\w+:\w+[\[\]\w]+[, \w\]]+)[,|\)]
        # in : def __init__(self, submissions:list[Submission, L_1_0_2], application_number:str, sponsor_name:str, openfda:Openfda, products:list[Product]):
        # match 1: submissions:list[Submission, L_1_0_2] 2: application_number:str etc
        # old regex, does not work for nested classes, but easier on the eyes
        # (\w+:[\w\[\]]+)
        properties = re.findall(r'(\w+:\w+[\[\]\w]+[, \w\]]+)[,|\)]', init)
        for p in properties:
            numClass = 0 # for unequal nested dicts
            for classname in classnames:
                if classname in p:            
                    context = re.findall(r'(\w+):', p)[0] # finds match 1: submissions
                    if numClass > 0: # will append the number of the nested class
                        context += f'_{numClass}'
                    classcontext[classname] = context
                    numClass += 1
    return classcontext

def replace_root_test(testcode:str, newName:str, oldname:str='') -> str:
    root_name = re.findall(r'.*root = (.+).from_dict', testcode)[0]
    if oldname:
        if oldname == root_name:
            testcode = testcode.replace(root_name, newName)
    else:
        testcode = testcode.replace(root_name, newName)
    return testcode

def auto_rename(code:str, testcode:str='')->dict:
    classnames = find_classes(code)
    inits = find_inits_for_classes(code, classnames)
    contexts = find_class_contexts(classnames, inits)
    contexts[classnames[0]] = 'Root'

    for classname in contexts.keys():
        context = contexts[classname].capitalize()
        if context[-1] == 's': # remove trailing s
            context = context[:-1]
            if context[-2:] == 'ie': # convert english plural to singular
                context = context[:-2] + 'y'

        code = rename_class(classname, context, code)
        if testcode:
            testcode = rename_class(classname, context, testcode)

    return {'code':code, 'test':testcode}

def to_safe_key(key:str) -> str:
    if key in py_keywords_conv.keys():
        safe_key = py_keywords_conv[key]
    else:
        safe_key = key

    return safe_key
    
# deprec function, kept for documentation
def decode_layer_re(data:dict, classname:str='', layerdepth:int=0) -> list[CodeBlock]:
    """
        Pre Refactor: Function decodes the current dictionary, recursively decodes any contained dictionaries \n
        Generates code for classes with \n
        __init__() \n
        to_dict() \n
        from_dict() \n

        \n
        class ?: \n
            __init__(self,?): \n
            to_dict(self):  \n
            from_dict(cls,?):   \n

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
        safe_key = to_safe_key(key)
        val = data[key]
        valtype = type(val)
        typestr = valtype.__name__ 
        todict_body_str = f'"{key}": self.{safe_key}, '
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
                            nthclassblocklist = decode_layer_re(element, classname=classstr, layerdepth=layerdepth+1)
                            codeblocks += nthclassblocklist
                            uniquedicts += 1

                    else:
                        classstr = f'L_{layerdepth}_{keynum}_{dictnum}'
                        lastdict = element
                        uniquedicts += 1
                        nthclassblocklist = decode_layer_re(element, classname=classstr, layerdepth=layerdepth+1)
                        codeblocks += nthclassblocklist
                        if nthclassblocklist:
                            addlisttype = f'[{classstr}]'
                        else:
                            addlisttype = f'[dict]'
                        
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
                    todict_body_str = f'"{key}": [x.to_dict() for x in self.{safe_key}], '

                else:
                    typestr += f'[{elementtype.__name__}]'
                    todict_body_str = f'"{key}": self.{safe_key}, '

            # gets tricky here, heterogenous list -> unsolved

        # if theres a dict decode that dict with layerdepth + 1
        if valtype == type({}):
            typestr = f'L_{layerdepth}_{keynum}'
            nthclassblocklist = decode_layer_re(val, classname=typestr, layerdepth=layerdepth+1)
            codeblocks += nthclassblocklist
            if nthclassblocklist:
                todict_body_str = f'"{key}": self.{safe_key}.to_dict(), '
                from_dict_body_ifbody_returnstr_tmp = f'{typestr}.from_dict(data["{key}"]), '
            else:
                todict_body_str = f'"{key}": self.{safe_key}, '
                from_dict_body_ifbody_returnstr_tmp = f'data["{key}"], '
                typestr = f'dict'               
   
        inithead += f', {safe_key}:{typestr}'
        
        todict_body += todict_body_str
        blockstr = f'self.{safe_key} = {safe_key}'
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
    eq_code = pyt.make_eq_block()
    todict_code = CodeBlock(todict_head, [todict_body])
    fromdict_code_if = CodeBlock(from_dict_body_if, from_dict_body_if_lists + [from_dict_body_ifbody_returnstr])
    fromdict_code_else = CodeBlock(from_dict_body_else, [from_dict_body_elsebody])
    fromdict_code = CodeBlock(from_dict_head, [fromdict_code_if, fromdict_code_else])
    classcodeblock = CodeBlock(classhead, [initcodepy, eq_code, todict_code, '@classmethod', fromdict_code])
    if keynum > 0: # if dict wasnt empty
        codeblocks.append(classcodeblock)
    return codeblocks
    