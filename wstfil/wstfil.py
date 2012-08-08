import ply.lex as lex

class WST:
    def __init__(self,lang):
        self.lang = lang

    def translate(self,data):
        lexer = self.build_lexer()
        while True:
            tok = lexer.token()
            if not tok: break
            print tok
            
        
    def build_lexer(self):
        __import__("wstfil.rules."+self.lang)
        return lex.lex()
