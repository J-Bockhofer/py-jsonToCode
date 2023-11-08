import unittest
from templating.codeblock import CodeBlock
from jtc_core import decode_layer, json_to_code, dict_to_code

import os
import json

class TestTemplating(unittest.TestCase):

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

    def test_decode_layer_1(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4']
        }

        result = decode_layer(sampleDict)

        expected = f'''\
class L_0:
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
    def to_dict(self)->dict:
        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data:
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"])
        else:
            raise KeyError("Invalid data for L_0")
'''
        self.maxDiff = None
        self.assertEqual(result[-1].__str__(), expected)

    def test_decode_layer_2(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4'],
        'L1_Key4':{'L2_Key1':'L2Obj', 'L2_Key2': [5,6,7,8]},
        'L1_Key5':[{'L3_Key1':'L3Obj', 'L3_Key2': [34,6,546,8]},{'L4_Key1':'L4Obj', 'L4_Key2': [34,6,546,8]}],
        }

        result = decode_layer(sampleDict)

        expected = f'''\
class L_0:
    def __init__(self, L1_Key1:str, L1_Key2:list[int], L1_Key3:list[str], L1_Key4:L_0_3, L1_Key5:list[dict]):
        self.L1_Key1 = L1_Key1
        self.L1_Key2 = L1_Key2
        self.L1_Key3 = L1_Key3
        self.L1_Key4 = L1_Key4
        self.L1_Key5 = L1_Key5
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
        self.maxDiff = None
        self.assertEqual(result[-1].__str__(), expected)

    def test_decode_layer_nested(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4'],
        'L1_Key4':{'L2_Key1':'L2Obj', 'L2_Key2': [5,6,7,8]},
        'L1_Key5':[{'L3_Key1':'L3Obj', 'L3_Key2': [34,6,546,8]},{'L4_Key1':'L4Obj', 'L4_Key2': [34,6,546,8]}],
        }

        result = decode_layer(sampleDict)

        expected = f'''\
class L_0_3:
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
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
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()

        self.maxDiff = None
        self.assertEqual(fulltxt, expected)

    def test_decode_layer_nested2(self):
        sampleDict = {'L1_Key1':'Object1', 
        'L1_Key2':[1,2,3,4], 
        'L1_Key3':['s1','s2','s3','s4'],
        'L1_Key4':{'L2_Key1':'L2Obj', 'L2_Key2': [5,6,7,8]},
        'L1_Key5':[{'L3_Key1':'L3Obj', 'L3_Key2': [34,6,546,8]},{'L3_Key1':'L4Obj', 'L3_Key2': [34,6,546,8]}],
        }

        result = decode_layer(sampleDict)

        expected = f'''\
class L_0_3:
    def __init__(self, L2_Key1:str, L2_Key2:list[int]):
        self.L2_Key1 = L2_Key1
        self.L2_Key2 = L2_Key2
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
    def to_dict(self)->dict:
        return {{"L3_Key1": self.L3_Key1, "L3_Key2": self.L3_Key2}}
    @classmethod
    def from_dict(cls, data:dict):
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
    def to_dict(self)->dict:
        return {{"L1_Key1": self.L1_Key1, "L1_Key2": self.L1_Key2, "L1_Key3": self.L1_Key3, "L1_Key4": self.L1_Key4.to_dict(), "L1_Key5": [x.to_dict() for x in self.L1_Key5]}}
    @classmethod
    def from_dict(cls, data:dict):
        if "L1_Key1" in data and "L1_Key2" in data and "L1_Key3" in data and "L1_Key4" in data and "L1_Key5" in data:
            classlist_L1_Key5 = [L_0_4_1.from_dict(classdata) for classdata in data.get("L1_Key5", [])]
            return cls(data["L1_Key1"], data["L1_Key2"], data["L1_Key3"], L_0_3.from_dict(data["L1_Key4"]), classlist_L1_Key5)
        else:
            raise KeyError("Invalid data for L_0")
'''
        fulltxt = ''
        for res in result:
            fulltxt += res.__str__()

        self.maxDiff = None
        self.assertEqual(fulltxt, expected)

    def test_find_classes(self):
        pass
      

if __name__ == '__main__':
    unittest.main()