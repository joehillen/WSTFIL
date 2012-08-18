import ply.lex as lex
import ply.yacc as yacc
from pprint import pprint
import re

from lexer import WSTLexer

def generate(tree):
    result = ""
    for l in tree:
        t = l[0] # t is for type
        if t == "echo":
            result += l[1]
        elif t == "line":
            result += l[1] + ";" + l[2]
        elif t == "block":
            start = l[1]
            nl = l[2]
            inner = l[3]
            result += start + " {" + nl
            innertext = generate(inner)
            for line in innertext.split('\n'):
                if len(line.rstrip())>0:
                    result += "    " + line.rstrip() + '\n'
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

            
        
