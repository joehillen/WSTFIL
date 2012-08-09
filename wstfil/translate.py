import ply.lex as lex

def translate(lang,data):
    rules = __import__("rules."+lang,globals(),locals(),["c"],-1)
    lexer = lex.lex(module=rules,debug=1)
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break
        print tok
            
        
