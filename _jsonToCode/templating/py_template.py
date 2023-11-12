from .codeblock import CodeBlock

import re
# Example Root Class
# 'class L_0:'
#    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:dict):
#        self.L1_Key1 = L1_Key1
#        self.L1_Key2 = L1_Key2
#        self.L1_Key3 = L1_Key3
#    def __eq__(self, other):
#        return self.to_dict() == other
#    def __str__(self):
#        return f'L1_Key1 = {self.L1_Key1}, L1_Key2 = {self.L1_Key2}, L1_Key3 = {self.L1_Key3}
#    def to_dict(self)->dict:
#        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3}}
#    @classmethod
#    def from_dict(cls, data:dict):
#        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data:
#            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"])
#        else:
#            raise KeyError("Invalid data for L_0")

def make_init_block(safekeys:list[str], types:list[str])->CodeBlock:
    """
        takes a list of safekeys and associated types \n
        generates the __init__ CodeBlock \n
    """
    if len(safekeys) != len(types):
        raise ValueError("List of safekeys and list of types are not the same length")

    inithead = f'def __init__(self'
    initblock = []

    for i in range(0, len(safekeys)):
        inithead += f', {safekeys[i]}:{types[i]}'
        initblock.append(f'self.{safekeys[i]} = {safekeys[i]}')
    inithead += f')'

    return CodeBlock(inithead, initblock)

def make_eq_block()->CodeBlock:
    eqhead = 'def __eq__(self, other)'
    eqbody = 'return self.to_dict() == other'
    return CodeBlock(eqhead,[eqbody])

def make_str_block(classname:str, safekeys:list[str], types:list[str])->CodeBlock:
    strhead = 'def __str__(self)'
    strbody= f"return f'{classname}: "
    strbodytmp = ''
    for i in range(0, len(safekeys)):
        safekey = safekeys[i]
        safekeystr = f'self.{safekey}'
        strbodytmp = f'{safekey} = {{{safekeystr}.__str__()}}, ' # triple braces to get evaluated
        if 'list[' in types[i]:
            strbodytmp = f'{safekey} = {{[x.__str__() for x in {safekeystr}]}}, '

        strbody += strbodytmp
    strbody = strbody[:-2] # remove , and whitespace
    strbody += "'" # add ' to end f-string

    return CodeBlock(strhead, [strbody])

def make_repr_block(classname:str, safekeys:list[str], types:list[str])->CodeBlock:
    reprhead = 'def __repr__(self)'
    reprbody = f'return f\'{classname}('
    for i in range(0, len(safekeys)):
        safekey = safekeys[i]
        safekeystr = f'self.{safekey}'
        reprbodytmp = f'{safekey}={{repr({safekeystr})}}, ' # triple braces to get evaluated
        #if 'list[' in types[i]:
        #    reprbodytmp = f'{safekey}={{[repr(x) for x in {safekeystr}]}}, '
        reprbody += reprbodytmp
    reprbody = reprbody[:-2] # remove , and whitespace
    reprbody += ")'"#.replace('\\\\', '')" # add )' to end class init and f-string

    return CodeBlock(reprhead, [reprbody])

def make_todict_block(inkeys:list[str], safekeys:list[str], types:list[str])->CodeBlock:
    """
        takes a list of original keys, safekeys and associated types \n
        generates the to_dict CodeBlock \n
    """
    if len(safekeys) != len(types) or len(safekeys) != len(inkeys):
        raise ValueError("Input lists are not the same length")

    todict_head = f'def to_dict(self)->dict'
    todict_body = 'return {'
    for i in range(0, len(safekeys)):
        todict_body_str = f'"{inkeys[i]}": self.{safekeys[i]}, '
        if 'list[L_' in types[i]:
            # list of classes
            todict_body_str = f'"{inkeys[i]}": [x.to_dict() for x in self.{safekeys[i]}], '
        elif 'list[' in types[i]:
            # homogenous list of something
            # should be same as default
            pass
        elif 'L_' in types[i]:
            # singular class dict
            todict_body_str = f'"{inkeys[i]}": self.{safekeys[i]}.to_dict(), '
        todict_body += todict_body_str

    todict_body = todict_body[:-2]
    todict_body += '}'

    return CodeBlock(todict_head, [todict_body])    

def make_fromdict_block(classname:str, 
                        inkeys:list[str],
                        types:list[str],
                        uniquedicts:list[int],
                        singledictlist:list[int],
                        classstrlist:list[str])->CodeBlock:
    """
        takes a classname, a list of original keys, associated types, \n 
        a list that says how many unique dicts contained list has \n
        a list that says if a singular contained dict was succesfully decoded (==1) \n
        a list with class strings for successfully decoded dicts \n
        generates the from_dict CodeBlock \n
    """
    from_dict_head = f'def from_dict(cls, data:dict)->\'{classname}\''
    from_dict_body_if = 'if ' # if object property1 in data and object property2 in data 
    from_dict_body_if_lists = []
    from_dict_body_ifbody_returnstr = 'return cls('
    from_dict_body_else = 'else'
    from_dict_body_elsebody = 'raise KeyError("Invalid data for '
    from_dict_body_elsebody_tmp = f'{classname}'

    for i in range(0, len(inkeys)):
        from_dict_body_ifbody_returnstr_tmp = f'data["{inkeys[i]}"], '
        from_dict_body_if += f'"{inkeys[i]}" in data and '
        #                                          ^12345^ 
        # delete these 5 chars after last iteration
        if 'list[L_' in types[i] or 'list[dict]' in types[i]:
            # list of classes
            if uniquedicts[i] == 1:
                from_dict_body_if_lists.append(f'classlist_{inkeys[i]} = [{classstrlist[i]}.from_dict(classdata) for classdata in data.get("{inkeys[i]}", [])]') 
                from_dict_body_ifbody_returnstr_tmp = f'classlist_{inkeys[i]}, '
                from_dict_body_elsebody_tmp = f'{classname}'   
            else:
                from_dict_body_if_lists.append(f'classlist_{inkeys[i]} = data["{inkeys[i]}"]')
                from_dict_body_ifbody_returnstr_tmp = f'classlist_{inkeys[i]}, '                
        elif 'list[' in types[i]:
            # homogenous list of something
            # should be same as default
            pass
        elif 'L_' in types[i]:
            # singular class dict
            if singledictlist[i]==1:
                from_dict_body_ifbody_returnstr_tmp = f'{types[i]}.from_dict(data["{inkeys[i]}"]), '
            elif singledictlist[i]==2:
                from_dict_body_ifbody_returnstr_tmp = f'data["{inkeys[i]}"], '
        from_dict_body_ifbody_returnstr += from_dict_body_ifbody_returnstr_tmp

    from_dict_body_if = from_dict_body_if[:-5]
    from_dict_body_ifbody_returnstr = from_dict_body_ifbody_returnstr[:-2]
    from_dict_body_ifbody_returnstr += ')'
    from_dict_body_elsebody += from_dict_body_elsebody_tmp + '")'   

    fromdict_code_if = CodeBlock(from_dict_body_if, from_dict_body_if_lists + [from_dict_body_ifbody_returnstr])
    fromdict_code_else = CodeBlock(from_dict_body_else, [from_dict_body_elsebody])

    return CodeBlock(from_dict_head, [fromdict_code_if, fromdict_code_else])

def make_fromrandom_block(classname:str, safekeys:list[str], types:list[str])->CodeBlock:
    # will need import random & string into serializer
    # define random generation
    randstr = '\'\'.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))'
    randint = 'random.randint(lowlim, uplim)'
    randfloat = 'random.uniform(lowlim, uplim)'
    randbool = 'bool(random.getrandbits(1))'
    randclassend = '.from_random(seed, lowlim, uplim)'
    _forliststr = ' for _ in range(lowlim, uplim)]' # for uniform lists

    # def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_2_1'
    from_rand_head = f'def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->\'{classname}\''
    from_rand_seedif = 'if seed'
    from_rand_seedbody = 'random.seed(seed)'
    from_rand_body = [CodeBlock(from_rand_seedif,[from_rand_seedbody])]
    from_rand_return = 'return cls('
    for i in range(0, len(safekeys)):
        ctype = types[i]
        cskey = safekeys[i]
        # add to return string
        from_rand_return += f'{cskey}, '
        # check types
        if ctype == 'int':
            from_rand_body.append(f'{cskey} = ' + randint)
        if ctype == 'str':
            from_rand_body.append(f'{cskey} = ' + randstr)
        if ctype == 'float':
            from_rand_body.append(f'{cskey} = ' + randfloat)
        if ctype == 'bool':
            from_rand_body.append(f'{cskey} = ' + randbool)          
        if ctype == 'dict':
            from_rand_body.append(f'{cskey} = {{}}')
        if 'list' in ctype:
            # its a typed list
            liststrtmp = f'{cskey} = ['
            listtype = re.findall(r'\[(.*)\]', ctype)
            if listtype:
                #typed list
                listtype = listtype[0]
                if listtype == 'int':
                    liststrtmp += randint + _forliststr
                if listtype == 'str':
                    liststrtmp += randstr + _forliststr
                if listtype == 'float':
                    liststrtmp += randfloat + _forliststr
                if listtype == 'bool':
                    liststrtmp += randbool + _forliststr                    
                if listtype == 'list':
                    liststrtmp += '[]' + _forliststr
                if listtype == 'dict':
                    liststrtmp += '{}' + _forliststr
                if 'L_' in listtype:
                    liststrtmp += f'{listtype}'+ randclassend +_forliststr
            else:
                liststrtmp += ']'
            from_rand_body.append(liststrtmp)
        elif 'L_' in ctype:
            # just a class, no need to panic
            from_rand_body.append(f'{cskey} = {ctype}' + randclassend)
    # cut whitespace + , from returnstring
    from_rand_return = from_rand_return[:-2]
    from_rand_return += ')'
    from_rand_body.append(from_rand_return)
    return CodeBlock(from_rand_head, from_rand_body)

def make_doc_string(classname:str, initblock:CodeBlock)->str:
    docstring = f'''\
"""
        {classname}:
        {initblock.head}
    """'''
    return docstring
