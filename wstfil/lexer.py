import ply.lex as lex

class WSTLexer(object):

    def __init__(self, module, debug):
        self.lexer = lex.lex(module=module,debug=debug)
        self.lexer.prev_ind = 0
        self.lexer.cur_ind = 0
        self.lexer.block_count = 0
        self.lexer.prepend = []

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        tok = self.lexer.token()
        self.lexer.prepend += [tok]
        return self.lexer.prepend.pop(0)
