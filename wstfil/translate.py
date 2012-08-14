import ply.lex as lex
import ply.yacc as yacc
from pprint import pprint

def generate(tree):
    result = ""
    for l in tree:
        t = l[0] # t is for type
        if t == "echo":
            result += l[1]
        elif t == "block":
            line = l[1]
            inner = l[2]
            result += line[1] + " {" + line[2]
            result += "    " + generate(inner)[:-1]
            result += "}\n"
        elif t == "line":
            result += l[1] + ";" + l[2]
    return result

def translate(lang,data):
    rules = __import__("rules."+lang,globals(),locals(),[lang],-1)
    lexer = lex.lex(module=rules,debug=1)
    lexer.prev_ind = 0
    lexer.cur_ind = 0
    lexer.input(data)
    print 'TOKENS:'
    while True:
        tok = lexer.token()
        if not tok: break
        print tok
    parser = rules.parser
    tree = parser.parse(data,debug=True)
    print "tree"
    pprint(tree)
    return generate(tree)

            
        
