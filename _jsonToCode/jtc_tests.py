import unittest
from templating.codeblock import CodeBlock
from jtc_core import decode_layer, decode_layer_re, json_to_code, dict_to_code, find_classes, find_inits_for_classes, find_class_contexts

import os
import json

class TestTemplating(unittest.TestCase):

# Simple test for CodeBlock generation
    def test_codeblock_simple(self):
        ifblock = CodeBlock('if x>0', ['print x', 'print "Finished."'])
        block = CodeBlock('def print_success(x)', [ifblock, 'print "Def finished."'])

        res = f'''\
def print_success(x):
    if x>0:
        print x
        print "Finished."
    print "Def finished."
'''

        self.assertEqual(block.__str__(), res)


# Test decode_layer with empty input
    def test_decode_layer_empty(self):
        sampleDict = {}

        result = decode_layer(sampleDict)

        expected = []
        self.maxDiff = None
        self.assertEqual(result, expected)

# Test decode_layer with nested list of unequal dict
    def test_decode_layer_nested_uneq(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4'],
        'L1_Key4':{'L2_Key1':'L2Obj', 'L2_Key2': [5,6,7,8]},
        'L1_Key5':[{'L3_Key1':'L3Obj', 'L3_Key2': [34,6,546,8]},{'L4_Key1':'L4Obj', 'L4_Key2': [34,6,546,8]}],
        }

        result = decode_layer(sampleDict)

        expected = '''\
class L_0_3_:
    """
        L_0_3_:
        def __init__(self, L2_Key1:str, L2_Key2:list[int])
    """
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_3_: L2_Key1 = {self.L2_Key1.__str__()}, L2_Key2 = {[x.__str__() for x in self.L2_Key2]}'
    def __repr__(self):
        return f'L_0_3_(L2_Key1={repr(self.L2_Key1)}, L2_Key2={repr(self.L2_Key2)})'
    def to_dict(self)->dict:
        return {"L2_Key1": self.L2_Key1, "L2_Key2": self.L2_Key2}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_3_':
        if "L2_Key1" in data and "L2_Key2" in data:
            return cls(data["L2_Key1"], data["L2_Key2"])
        else:
            raise KeyError("Invalid data for L_0_3_")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_3_':
        if seed:
            random.seed(seed)
        L2_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L2_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L2_Key1, L2_Key2)
class L_0_4_1:
    """
        L_0_4_1:
        def __init__(self, L3_Key1:str, L3_Key2:list[int])
    """
    def __init__(self, L3_Key1:str, L3_Key2:list[int]):
        self.L3_Key1 = L3_Key1
        self.L3_Key2 = L3_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_4_1: L3_Key1 = {self.L3_Key1.__str__()}, L3_Key2 = {[x.__str__() for x in self.L3_Key2]}'
    def __repr__(self):
        return f'L_0_4_1(L3_Key1={repr(self.L3_Key1)}, L3_Key2={repr(self.L3_Key2)})'
    def to_dict(self)->dict:
        return {"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_4_1':
        if "L3_Key1" in data and "L3_Key2" in data:
            return cls(data["L3_Key1"], data["L3_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_1")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_4_1':
        if seed:
            random.seed(seed)
        L3_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L3_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L3_Key1, L3_Key2)
class L_0_4_2:
    """
        L_0_4_2:
        def __init__(self, L4_Key1:str, L4_Key2:list[int])
    """
    def __init__(self, L4_Key1:str, L4_Key2:list[int]):
        self.L4_Key1 = L4_Key1
        self.L4_Key2 = L4_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_4_2: L4_Key1 = {self.L4_Key1.__str__()}, L4_Key2 = {[x.__str__() for x in self.L4_Key2]}'
    def __repr__(self):
        return f'L_0_4_2(L4_Key1={repr(self.L4_Key1)}, L4_Key2={repr(self.L4_Key2)})'
    def to_dict(self)->dict:
        return {"L4_Key1": self.L4_Key1, "L4_Key2": self.L4_Key2}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_4_2':
        if "L4_Key1" in data and "L4_Key2" in data:
            return cls(data["L4_Key1"], data["L4_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_2")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_4_2':
        if seed:
            random.seed(seed)
        L4_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L4_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L4_Key1, L4_Key2)
class L_0:
    """
        L_0:
        def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3_, L1_Key5:list[L_0_4_1, L_0_4_2])
    """
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3_, L1_Key5:list[L_0_4_1, L_0_4_2]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: L1_Key1 = {self.L1_Key1.__str__()}, L1_Key2 = {[x.__str__() for x in self.L1_Key2]}, L1_Key3 = {[x.__str__() for x in self.L1_Key3]}, L1_Key4 = {self.L1_Key4.__str__()}, L1_Key5 = {[x.__str__() for x in self.L1_Key5]}'
    def __repr__(self):
        return f'L_0(L1_Key1={repr(self.L1_Key1)}, L1_Key2={repr(self.L1_Key2)}, L1_Key3={repr(self.L1_Key3)}, L1_Key4={repr(self.L1_Key4)}, L1_Key5={repr(self.L1_Key5)})'
    def to_dict(self)->dict:
        return {"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            _classlist_L1_Key5 = ['L_0_4_1', 'L_0_4_2']
            classlist_L1_Key5 = [eval(_class).from_dict(x) for _class in _classlist_L1_Key5 for x in data["L1_Key5"] if eval(_class).from_random().to_dict().keys() == x.keys()]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3_.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0':
        if seed:
            random.seed(seed)
        L1_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L1_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        L1_Key3 = [''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim)) for _ in range(lowlim, uplim)]
        L1_Key4 = L_0_3_.from_random(seed, lowlim, uplim)
        L1_Key5 = [eval(random.choice(['L_0_4_1', 'L_0_4_2'])).from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L1_Key1, L1_Key2, L1_Key3, L1_Key4, L1_Key5)
'''
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()

        self.maxDiff = None
        self.assertEqual(fulltxt, expected)
# Test decode_layer with nested list of equal dict
    def test_decode_layer_nested_equal(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4'],
        'L1_Key4':{'L2_Key1':'L2Obj', 'L2_Key2': [5,6,7,8]},
        'L1_Key5':[{'L3_Key1':'L3Obj', 'L3_Key2': [34,6,546,8]},{'L3_Key1':'L4Obj', 'L3_Key2': [34,6,546,8]}],
        }

        result = decode_layer(sampleDict)

        expected = '''\
class L_0_3_:
    """
        L_0_3_:
        def __init__(self, L2_Key1:str, L2_Key2:list[int])
    """
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_3_: L2_Key1 = {self.L2_Key1.__str__()}, L2_Key2 = {[x.__str__() for x in self.L2_Key2]}'
    def __repr__(self):
        return f'L_0_3_(L2_Key1={repr(self.L2_Key1)}, L2_Key2={repr(self.L2_Key2)})'
    def to_dict(self)->dict:
        return {"L2_Key1": self.L2_Key1, "L2_Key2": self.L2_Key2}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_3_':
        if "L2_Key1" in data and "L2_Key2" in data:
            return cls(data["L2_Key1"], data["L2_Key2"])
        else:
            raise KeyError("Invalid data for L_0_3_")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_3_':
        if seed:
            random.seed(seed)
        L2_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L2_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L2_Key1, L2_Key2)
class L_0_4_1:
    """
        L_0_4_1:
        def __init__(self, L3_Key1:str, L3_Key2:list[int])
    """
    def __init__(self, L3_Key1:str, L3_Key2:list[int]):
        self.L3_Key1 = L3_Key1
        self.L3_Key2 = L3_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_4_1: L3_Key1 = {self.L3_Key1.__str__()}, L3_Key2 = {[x.__str__() for x in self.L3_Key2]}'
    def __repr__(self):
        return f'L_0_4_1(L3_Key1={repr(self.L3_Key1)}, L3_Key2={repr(self.L3_Key2)})'
    def to_dict(self)->dict:
        return {"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_4_1':
        if "L3_Key1" in data and "L3_Key2" in data:
            return cls(data["L3_Key1"], data["L3_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_1")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0_4_1':
        if seed:
            random.seed(seed)
        L3_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L3_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L3_Key1, L3_Key2)
class L_0:
    """
        L_0:
        def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3_, L1_Key5:list[L_0_4_1])
    """
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3_, L1_Key5:list[L_0_4_1]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: L1_Key1 = {self.L1_Key1.__str__()}, L1_Key2 = {[x.__str__() for x in self.L1_Key2]}, L1_Key3 = {[x.__str__() for x in self.L1_Key3]}, L1_Key4 = {self.L1_Key4.__str__()}, L1_Key5 = {[x.__str__() for x in self.L1_Key5]}'
    def __repr__(self):
        return f'L_0(L1_Key1={repr(self.L1_Key1)}, L1_Key2={repr(self.L1_Key2)}, L1_Key3={repr(self.L1_Key3)}, L1_Key4={repr(self.L1_Key4)}, L1_Key5={repr(self.L1_Key5)})'
    def to_dict(self)->dict:
        return {"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            classlist_L1_Key5 = [L_0_4_1.from_dict(classdata) for classdata in data.get("L1_Key5", [])]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3_.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0':
        if seed:
            random.seed(seed)
        L1_Key1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        L1_Key2 = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        L1_Key3 = [''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim)) for _ in range(lowlim, uplim)]
        L1_Key4 = L_0_3_.from_random(seed, lowlim, uplim)
        L1_Key5 = [L_0_4_1.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        return cls(L1_Key1, L1_Key2, L1_Key3, L1_Key4, L1_Key5)
'''
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()

        self.maxDiff = None
        self.assertEqual(fulltxt, expected)

# Test decode_layer with nested empty dict
    def test_decode_layer_nested_empty(self):
        sampleDict = {
        'L1_Key1':{}
        }

        result = decode_layer(sampleDict)

        expected = '''\
class L_0:
    """
        L_0:
        def __init__(self, L1_Key1:dict)
    """
    def __init__(self, L1_Key1:dict):
        self.L1_Key1 = L1_Key1
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: L1_Key1 = {self.L1_Key1.__str__()}'
    def __repr__(self):
        return f'L_0(L1_Key1={repr(self.L1_Key1)})'
    def to_dict(self)->dict:
        return {"L1_Key1": self.L1_Key1}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "L1_Key1" in data:
            return cls(data["L1_Key1"])
        else:
            raise KeyError("Invalid data for L_0")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0':
        if seed:
            random.seed(seed)
        L1_Key1 = {}
        return cls(L1_Key1)
'''
        self.maxDiff = None
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()
        self.assertEqual(fulltxt, expected)

# Test decode_layer for json with pylang keys
    def test_decode_layer_nested_pylang(self):
        sampleDict = {'from':'Object1', 
        'range':[1,2,3,4], 
        'raise':'error259'
        }

        result = decode_layer(sampleDict)

        expected = '''\
class L_0:
    """
        L_0:
        def __init__(self, FROM:str, RANGE:list[int], RAISE:str)
    """
    def __init__(self, FROM:str, RANGE:list[int], RAISE:str):
        self.FROM = FROM
        self.RANGE = RANGE
        self.RAISE = RAISE
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: FROM = {self.FROM.__str__()}, RANGE = {[x.__str__() for x in self.RANGE]}, RAISE = {self.RAISE.__str__()}'
    def __repr__(self):
        return f'L_0(FROM={repr(self.FROM)}, RANGE={repr(self.RANGE)}, RAISE={repr(self.RAISE)})'
    def to_dict(self)->dict:
        return {"from": self.FROM, "range": self.RANGE, "raise": self.RAISE}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "from" in data and "range" in data and "raise" in data:
            return cls(data["from"], data["range"], data["raise"])
        else:
            raise KeyError("Invalid data for L_0")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'L_0':
        if seed:
            random.seed(seed)
        FROM = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        RANGE = [random.randint(lowlim, uplim) for _ in range(lowlim, uplim)]
        RAISE = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(FROM, RANGE, RAISE)
'''
        self.maxDiff = None
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()
        self.assertEqual(fulltxt, expected)

# Test find classes in code
    def test_find_classes(self):
        text = f'''\
class L_0_3:
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L2_Key1": self.L2_Key1, "L2_Key2": self.L2_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L2_Key1" in data and "L2_Key2" in data:
            return cls(data["L2_Key1"], data["L2_Key2"])
        else:
            raise KeyError("Invalid data for L_0_3")
class L_0_4_1:
    def __init__(self, L3_Key1:str, L3_Key2:list[int]):
        self.L3_Key1 = L3_Key1
        self.L3_Key2 = L3_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L3_Key1" in data and "L3_Key2" in data:
            return cls(data["L3_Key1"], data["L3_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_1")
class L_0_4_2:
    def __init__(self, L4_Key1:str, L4_Key2:list[int]):
        self.L4_Key1 = L4_Key1
        self.L4_Key2 = L4_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L4_Key1": self.L4_Key1, "L4_Key2": self.L4_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L4_Key1" in data and "L4_Key2" in data:
            return cls(data["L4_Key1"], data["L4_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_2")
class L_0:
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3, L1_Key5:list[dict]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            classlist_L1_Key5 = data["L1_Key5"]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
'''        
        classes = find_classes(text)
        expected = ['L_0', 'L_0_3', 'L_0_4_1', 'L_0_4_2']

        self.assertEqual(classes, expected)
# Test find inits in code
    def test_find_inits(self):
        text = f'''\
class L_0_3:
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L2_Key1": self.L2_Key1, "L2_Key2": self.L2_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L2_Key1" in data and "L2_Key2" in data:
            return cls(data["L2_Key1"], data["L2_Key2"])
        else:
            raise KeyError("Invalid data for L_0_3")
class L_0_4_1:
    def __init__(self, L3_Key1:str, L3_Key2:list[int]):
        self.L3_Key1 = L3_Key1
        self.L3_Key2 = L3_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L3_Key1" in data and "L3_Key2" in data:
            return cls(data["L3_Key1"], data["L3_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_1")
class L_0_4_2:
    def __init__(self, L4_Key1:str, L4_Key2:list[int]):
        self.L4_Key1 = L4_Key1
        self.L4_Key2 = L4_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L4_Key1": self.L4_Key1, "L4_Key2": self.L4_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L4_Key1" in data and "L4_Key2" in data:
            return cls(data["L4_Key1"], data["L4_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_2")
class L_0:
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3, L1_Key5:list[dict]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
    def __eq__(self, other):
        return self.to_dict() == other
    def to_dict(self)->dict:
        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            classlist_L1_Key5 = data["L1_Key5"]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
'''        
        classes = find_classes(text)
        inits = find_inits_for_classes(text, classes)
        expected = [
            'def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3, L1_Key5:list[dict])', 
            'def __init__(self, L2_Key1:str, L2_Key2:list[int])', 
            'def __init__(self, L3_Key1:str, L3_Key2:list[int])', 
            'def __init__(self, L4_Key1:str, L4_Key2:list[int])']
        self.maxDiff = None
        self.assertEqual(inits, expected)    
# Test find contexts in code
    def test_find_contexts(self):
        text = f'''\
class L_0_3:
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_3: L2_Key1 = {{self.L2_Key1.__str__()}}, L2_Key2 = {{[x.__str__() for x in self.L2_Key2]}}'
    def __repr__(self):
        return f'L_0_3(L2_Key1={{repr(self.L2_Key1)}}, L2_Key2={{repr(self.L2_Key2)}})'
    def to_dict(self)->dict:
        return {{"L2_Key1": self.L2_Key1, "L2_Key2": self.L2_Key2}}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_3':
        if "L2_Key1" in data and "L2_Key2" in data:
            return cls(data["L2_Key1"], data["L2_Key2"])
        else:
            raise KeyError("Invalid data for L_0_3")
class L_0_4_1:
    def __init__(self, L3_Key1:str, L3_Key2:list[int]):
        self.L3_Key1 = L3_Key1
        self.L3_Key2 = L3_Key2
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0_4_1: L3_Key1 = {{self.L3_Key1.__str__()}}, L3_Key2 = {{[x.__str__() for x in self.L3_Key2]}}'
    def __repr__(self):
        return f'L_0_4_1(L3_Key1={{repr(self.L3_Key1)}}, L3_Key2={{repr(self.L3_Key2)}})'
    def to_dict(self)->dict:
        return {{"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}}
    @classmethod
    def from_dict(cls, data:dict)->'L_0_4_1':
        if "L3_Key1" in data and "L3_Key2" in data:
            return cls(data["L3_Key1"], data["L3_Key2"])
        else:
            raise KeyError("Invalid data for L_0_4_1")
class L_0:
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3, L1_Key5:list[L_0_4_1]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
    def __eq__(self, other):
        return self.to_dict() == other
    def __str__(self):
        return f'L_0: L1_Key1 = {{self.L1_Key1.__str__()}}, L1_Key2 = {{[x.__str__() for x in self.L1_Key2]}}, L1_Key3 = {{[x.__str__() for x in self.L1_Key3]}}, L1_Key4 = {{self.L1_Key4.__str__()}}, L1_Key5 = {{[x.__str__() for x in self.L1_Key5]}}'
    def __repr__(self):
        return f'L_0(L1_Key1={{repr(self.L1_Key1)}}, L1_Key2={{repr(self.L1_Key2)}}, L1_Key3={{repr(self.L1_Key3)}}, L1_Key4={{repr(self.L1_Key4)}}, L1_Key5={{repr(self.L1_Key5)}})'
    def to_dict(self)->dict:
        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}}
    @classmethod
    def from_dict(cls, data:dict)->'L_0':
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            classlist_L1_Key5 = [L_0_4_1.from_dict(classdata) for classdata in data.get("L1_Key5", [])]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
'''                
        classes = find_classes(text)
        inits = find_inits_for_classes(text, classes)
        contexts = find_class_contexts(classes, inits)

        expected = {'L_0_3':'L1_key4', 'L_0_4_1':'L1_key5'} # key lowercase bc of .capitalize()

        self.maxDiff = None
        self.assertEqual(contexts, expected)               

if __name__ == '__main__':
    unittest.main()