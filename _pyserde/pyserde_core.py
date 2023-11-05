from templating.codeblock import CodeBlock
from templating.filewriter import generate_file

import json
import os

def decode_layer(data:dict, classname:str='', layerdepth:int=0) -> list[CodeBlock]:
    fieldnames = data.keys()
    values = data.values()
    
    if classname == '':
        classname += f'L_{layerdepth}'

    classhead = f'class {classname}'

    initblock = []
    codeblocks = []

    todict_head = f'def to_dict(self)->dict'
    todict_body = 'return {'

    keynum = 0
    inithead = f'def __init__(self'
    for key in data:
        
        val = data[key]
        valtype = type(val)
        typestr = valtype.__name__ 
        todict_body_str = f'"{key}": self.{key}, '
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
                        if lastdict.keys() != element.keys():
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
                        
                    else:
                        typestr += f'[{elementtype.__name__}]'
                    todict_body_str = f'"{key}": [x.to_dict() for x in self.{key}], '

                else:
                    typestr += f'[{elementtype.__name__}]'
                    todict_body_str = f'"{key}": self.{key}, '

            

        # if theres a dict decode that dict with layerdepth + 1
        if valtype == type({}):
            typestr = f'L_{layerdepth}_{keynum}'
            nthclassblocklist = decode_layer(val, classname=typestr, layerdepth=layerdepth+1)
            codeblocks += nthclassblocklist
            todict_body_str = f'"{key}": self.{key}.to_dict(), '
   
        inithead += f', {key}:{typestr}'
        
        todict_body += todict_body_str
        blockstr = f'self.{key} = {key}'
        initblock.append(blockstr)
        keynum += 1
    inithead += f')'
    todict_body = todict_body[:-1]
    todict_body = todict_body[:-1]
    todict_body += '}'

    initcodepy = CodeBlock(inithead, initblock)
    todict_code = CodeBlock(todict_head, [todict_body])
    classcodeblock = CodeBlock(classhead, [initcodepy, todict_code])
    codeblocks.append(classcodeblock)
    return codeblocks


def dict_to_code(data:dict, filename:str):
    result = decode_layer(data)
    fulltxt = ''
    for res in result:
        fulltxt += res.__str__()

        with open(filename, 'w') as f:
            f.write(fulltxt)

def json_to_code(jsonfilename:str, codefilename:str):
    if os.path.exists(jsonfilename):
        with open(jsonfilename, "r", encoding='utf-8-sig') as data_file:
            data = json.load(data_file)  

    dict_to_code(data, codefilename)

    
    