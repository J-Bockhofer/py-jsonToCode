
py_keywords_conv = {
    """
        Definitions for Python language-safe keyword conversion
        key = keyword in Python (would break generated code)
        value = safe conversion product
    """
    # import
    'import':'IMPORT',
    'from' : 'FROM',
    'as' : 'AS',
    'global':'GLOBAL',    
    'nonlocal':'NONLOCAL',

    # def
    'class': 'CLASS',
    'def' : 'DEF',
    'with': 'WITH',

    # conditional
    'if':'IF',
    'else':'ELSE',
    'elif':'ELIF',
    'and':'AND',
    'or':'OR',
    'not':'NOT',

    # error handling
    'try':'TRY',
    'except':'EXCEPT',
    'raise':'RAISE',

    # flow control
    'for':'FOR',
    'return':'RETURN',
    'break':'BREAK',
    'while':'WHILE',
    'continue':'CONTINUE',
    'finally':'FINALLY',
    'yield':'YIELD',
    'pass':'PASS',

    #func
    'type':'TYPE',
    'len':'LEN',
    'is':'IS',
    'in':'IN',
    'any':'ANY',
    'lambda':'LAMBDA',
    'del':'DEL',
    'await':'AWAIT',
    'assert':'ASSERT',
    'async':'ASYNC',

    #types
    'False':'FALSE',
    'True':'TRUE',
    'int':'INT',
    'float':'FLOAT',
    'complex':'COMPLEX',
    'str':'STR',
    'dict':'DICT',
    'list':'LIST',
    'range':'RANGE',
    'tuple':'TUPLE',
    'bytes':'BYTES',
    'memoryview':'MEMORYVIEW',
    'bool':'BOOL',
    'set':'SET',
    'fronzenset':'FRONZENSET',
}