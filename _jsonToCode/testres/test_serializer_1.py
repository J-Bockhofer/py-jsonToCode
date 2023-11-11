import unittest
import json
from serializer_1 import *

class TestSerializer(unittest.TestCase):
    def test_serializer(self):
        with open("testjson_1.json", "r", encoding="utf-8-sig") as data_file:
            data = json.load(data_file)
        root = Cart.from_dict(data)
        data_b = root.to_dict()
        self.maxDiff = None
        self.assertEqual(data, data_b)
if __name__ == "__main__":
    unittest.main()
