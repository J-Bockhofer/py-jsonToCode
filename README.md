# py-jsonToCode

Zero dependency package to generate code for type safe Python serialization classes from .json files. \
Does not use dataclasses, but not tested on Python < 3.9. 

- Generates Code from .json
- Generates Unittest for the Serializer
- Simple CLI for renaming of classes and code generation

## Usage:

Run: `python example.py` from `./_jsonToCode` \
Edit the script to point to your json 

Or implement these lines anywhere:
```python

import jtc_core as jtc

jsonfile = './testres/testjson_1.json' # point to your .json
codetofile = './example_serializer.py' # file to create the code in

# generate the serializer
jsoncode = jtc.json_to_code(jsonfile, codetofile, encoding='utf-8-sig')

# optionally generate a unittest for the serializer
testcode, testfile = jtc.generate_test(jsonfile, codetofile)

# rename the classes 
from jtc_cli import cli_quick_rename

cli_quick_rename(codetofile, testfile)

```
\
Once generated, serialize a json by opening it \
and calling the `.from_dict()` method of the main class \
(default name: L_0)

```python
from testres.serializer_2 import *

with open("./testres/testjson_2.json", "r", encoding="utf-8-sig") as data_file:
    data = json.load(data_file)
root = L_0.from_dict(data)

```
\
Generated test for a serializer can be run by entering:\
`python testres/test_serializer_1.py`\
\
Package also includes unittests for code generation and class renaming patterns.\
`python jtc_tests.py`\
\
Alternatively you can use the basic CLI to generate code.\
The CLI is also used for renaming.

Run: `python jtc_cli.py`\
Type:   _g_ or _0_ for generating code\
or  :   _r_ or _1_ for renaming classes in generated code


### Generated Class example (./testres/serializer_1.py):
```python
class Root:
    """
        Root:
        def __init__(self, user:User, products:list[Product], timestamp:str)
    """
    def __init__(self, user:User, products:list[Product], timestamp:str):
        self.user = user
        self.products = products
        self.timestamp = timestamp
    def __eq__(self, other):
    def __str__(self):
        return f'Root: user = {self.user.__str__()}, products = {[x.__str__() for x in self.products]}, timestamp = {self.timestamp.__str__()}'
    def __repr__(self):
        return f'Root(user={repr(self.user)}, products={repr(self.products)}, timestamp={repr(self.timestamp)})'
    def to_dict(self)->dict:
        return {"user": self.user.to_dict(), "products": [x.to_dict() for x in self.products], "timestamp": self.timestamp}
    @classmethod
    def from_dict(cls, data:dict)->'Root':
        if "user" in data and "products" in data and "timestamp" in data:
            classlist_products = [Product.from_dict(classdata) for classdata in data.get("products", [])]
            return cls(User.from_dict(data["user"]), classlist_products, data["timestamp"])
        else:
            raise KeyError("Invalid data for Root")
    @classmethod
    def from_random(cls, seed:int=None, lowlim:int=1, uplim:int=10)->'Root':
        if seed:
            random.seed(seed)
        user = User.from_random(seed, lowlim, uplim)
        products = [Product.from_random(seed, lowlim, uplim) for _ in range(lowlim, uplim)]
        timestamp = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(lowlim, uplim))
        return cls(user, products, timestamp)
```

### Generated Test example (./testres/test_serializer_1.py):
```python
import unittest
import json
from serializer_1 import *

class TestSerializer(unittest.TestCase):
    def test_serializer(self):
        with open("testjson_1.json", "r", encoding="utf-8-sig") as data_file:
            data = json.load(data_file)
        root = Root.from_dict(data)
        data_b = root.to_dict()
        self.maxDiff = None
        self.assertEqual(data, data_b)
    
    def test_repr(self):
        with open("testjson_1.json", "r", encoding="utf-8-sig") as data_file:
            data = json.load(data_file)
        root = Root.from_dict(data)
        root_b = eval(repr(root))
        self.maxDiff = None
        self.assertEqual(root, root_b)
    
    def test_rand(self):
        root = Root.from_random()
        root_b = eval(repr(root))
        self.maxDiff = None
        self.assertEqual(root, root_b)
if __name__ == "__main__":
    unittest.main()

```