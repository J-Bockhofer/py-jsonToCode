import unittest
import json
from serializer_2 import *

class TestSerializer(unittest.TestCase):
    def test_serializer(self):
        with open("testjson_2.json", "r", encoding="utf-8-sig") as data_file:
            data = json.load(data_file)
        root = Root.from_dict(data)
        data_b = root.to_dict()
        self.maxDiff = None
        self.assertEqual(data, data_b)
    
    def test_repr(self):
        with open("testjson_2.json", "r", encoding="utf-8-sig") as data_file:
            data = json.load(data_file)
        root = Root.from_dict(data)
        root_b = eval(repr(root))
        self.maxDiff = None
        self.assertEqual(root, root_b)
if __name__ == "__main__":
    unittest.main()
