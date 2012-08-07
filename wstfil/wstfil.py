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
        if self.lang == "c":
            from rules import c
        return lex.lex()
