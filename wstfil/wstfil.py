import ply.lex as lex

class WST:
    def __init__(self,lang):
        self.lang = lang
        rules = __import__("rules."+self.lang,globals(),locals(),["c"],-1)
        self.lexer = lex.lex(module=rules,debug=1)

    def translate(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            print tok
            if not tok: break
            print tok
            
        
