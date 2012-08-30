import ply.lex as lex
import ply.yacc as yacc
from pprint import pprint
import re

from lexer import WSTLexer

def generate(tree):
    result = ""
    for l in tree:
        t = l[0] # t is for type
        if t == "echo" or t == "blank":
            result += l[1] + "\n"
        elif t == "line":
            result += l[1] + ";\n"
        elif t == "block":
            start = l[1]
            inner = l[2]
            result += start + "\n{\n"
            innertext = generate(inner)
            lines = innertext.split('\n')
            for line in lines[:-1]:
                result += "    " + line.rstrip() + '\n'
            last = lines[-1]
            if len(last.strip()) > 0:
                result += "    " + last.rstrip() + "\n"
                result += "}\n"
            else:
                result += "}\n"
    return result

def translate(lang,data):
    rules = __import__("rules."+lang,globals(),locals(),[lang],-1)

    # test lexer
    lexer = WSTLexer(module=rules,debug=True)
    lexer.input(data)
    print
    print 'TOKENS:'
    while True:
        tok = lexer.token()
        if not tok: break
        print tok
    print

    # do it for real
    lexer = WSTLexer(module=rules,debug=True)
    lexer.input(data)
    parser = rules.parser
    tree = parser.parse(lexer=lexer,input=data,debug=True)
    print "Tree:"
    pprint(tree)
    return generate(tree)

            
        
