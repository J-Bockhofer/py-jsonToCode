import jtc_core as jtc

import os
import readline

def main():
    readline.parse_and_bind('tab: complete')
    print("     jsonToCode CLI      ")
    cli_choose_mode()

def cli_choose_mode():
    gensymb = ['0','g']
    rensymb =['1','r']
    print(" Modes                   symbol")
    print("Generate Serializer :    0, g")
    print("Rename Classes :         1, r")    
    print("Choose mode by entering the symbol")
    mode = input()
    if mode in gensymb:
        cli_json_to_code()
    elif mode in rensymb:
        cli_rename_classes()
    else:
        cli_choose_mode()

def cli_json_to_code():
    jsonpath = user_get_jsonpath()
    encoding = user_get_encoding()
    pathq = "Enter the full filename for the resulting code (.py!)"
    codepath = user_get_codepath(pathq)
    serdecode = jtc.json_to_code(jsonpath, codepath, encoding)
    print(f'Code generated @{codepath}')
    question = 'Do you wish to generate a test for the serializer?'
    genyn = user_yn(question)
    if genyn == 'y':
        testcode, testfile = jtc.generate_test(jsonpath, codepath, encoding)
    question = 'Automatically rename the classes of the serializer?'
    autorename = user_yn(question)
    if autorename == 'y':
        res = jtc.auto_rename(serdecode, testcode)
        serdecode = res['code']
        testcode = res['test']

    question = 'Do you wish to manually rename the classes of the serializer?'
    renameyn = user_yn(question)

    while renameyn == 'y':
        serdecode, newname, oldname = user_rename_class(serdecode)
        if testcode:
            testcode = jtc.replace_root_test(testcode,newname,oldname)
        question = 'Keep renaming?'
        renameyn = user_yn(question)

    jtc.write_to_file(serdecode, codepath)
    if testcode:
        jtc.write_to_file(testcode, testfile)
    
def cli_rename_classes():
    pathq = "Enter the full filename for the serializer:"
    codepath = user_get_codepath(pathq)
    serdecode = jtc.text_from_file(codepath)
    question = 'Is there an associated test?'
    testyn = user_yn(question)
    if testyn == 'y':
        pathq = "Enter the full filename for the serializer test:"
        testpath = user_get_codepath(pathq)
        testcode = jtc.text_from_file(testpath)
    renameyn = 'y'
    question = 'Automatically rename the classes of the serializer?'
    autorename = user_yn(question)
    if autorename == 'y':
        res = jtc.auto_rename(serdecode, testcode)
        serdecode = res['code']
        testcode = res['test']
        question = 'Manually rename?'
        renameyn = user_yn(question)  
    while renameyn == 'y':
        serdecode, newname, oldname = user_rename_class(serdecode)
        if testcode:
           testcode = jtc.replace_root_test(testcode,newname,oldname)
        question = 'Keep renaming?'
        renameyn = user_yn(question)
    jtc.write_to_file(serdecode, codepath)
    if testcode:
        jtc.write_to_file(testcode, testpath)  

def cli_quick_rename(codepath:str, testpath:str=''):
    readline.parse_and_bind('tab: complete')
    serdecode = jtc.text_from_file(codepath)
    if testpath:
        testcode = jtc.text_from_file(testpath)
    renameyn = 'y'
    question = 'Automatically rename the classes of the serializer?'
    autorename = user_yn(question)
    if autorename == 'y':
        res = jtc.auto_rename(serdecode, testcode)
        serdecode = res['code']
        testcode = res['test']
        question = 'Manually rename?'
        renameyn = user_yn(question)
    while renameyn == 'y':
        serdecode, newname, oldname = user_rename_class(serdecode)
        if testcode:
           testcode = jtc.replace_root_test(testcode,newname,oldname)
        question = 'Keep renaming?'
        renameyn = user_yn(question)
    jtc.write_to_file(serdecode, codepath)
    if testcode:
        jtc.write_to_file(testcode, testpath)     
 

def user_get_jsonpath() -> str:
    print("Enter the full filename for the JSON file:")
    jsonpath = input()
    if os.path.exists(jsonpath):
        return jsonpath
    else:
        print(f'No .json file found @{jsonpath}')
        jsonpath = user_get_jsonpath()
        return jsonpath

def user_get_encoding() -> str:
    print("Enter the encoding (leave blank for 'utf-8-sig'):")
    encoding = input()
    if not encoding:
        encoding = 'utf-8-sig'
    if True: # empty check for valid encoding signatures
        return encoding
    else:
        encoding = user_get_encoding()
        return encoding

def user_get_codepath(question) -> str:
    print(question)
    codefile = input()
    path, file = os.path.split(os.path.abspath(codefile))
    if os.path.exists(path):
        return codefile
    else:
        print(f'Invalid path @{path}')
        codefile = user_get_codepath(question)
        return codefile    

def user_yn(question:str) -> str:
    anslist_y = ['y','Y','yes']
    anslist_n = ['n','N','no']
    print(question + '\nType y or n:')
    ans = input()
    
    if ans in anslist_y:
        return 'y'
    elif ans in anslist_n:
        return 'n'
    else:
        print("Enter yes or no ...")
        ans = user_yn(question)
        return ans

def user_get_new_name(oldname:str)-> str:
    print(f'Enter new name for {oldname}')
    newname = input()
    if newname:
        question = f'Rename {oldname} to {newname}?'
        ans = user_yn(question)
        if ans == 'y':
            return newname
    newname = user_get_new_name(oldname)
    return newname

def user_get_class(classnames:list[str])->str:
    print("Class names:")
    print(classnames)
    print("Enter a class name:")
    cname = input()
    if cname in classnames:
        return cname
    else:
        cname = user_get_class(classnames)
        return cname

def user_rename_class(serdecode:str):
    classnames = jtc.find_classes(serdecode)
    inits = jtc.find_inits_for_classes(serdecode, classnames)
    print("Found:")
    for i in range(0,len(classnames)):
        print(f'class:  {classnames[i]} \n {inits[i]}\n')
    oldname = user_get_class(classnames)
    cidx = classnames.index(oldname)
    print(f'Selected {oldname} with {inits[cidx]}')
    newname = user_get_new_name(oldname)
    serdecode = serdecode.replace(oldname, newname)
    return serdecode, newname, oldname


if __name__ == '__main__':
    main()