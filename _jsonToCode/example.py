import jtc_core as jtc

jsonfile = './testres/testjson_1.json'
codetofile = './example_serializer.py'

jsoncode = jtc.json_to_code(jsonfile, codetofile, encoding='utf-8-sig')
testcode, testfile = jtc.generate_test(jsonfile, codetofile)

# renaming of classes per ctrl+h or cli
from jtc_cli import cli_quick_rename

cli_quick_rename(codetofile, testfile)
