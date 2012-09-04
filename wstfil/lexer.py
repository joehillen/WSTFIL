import ply.lex as lex

class WSTLexer(object):

    def __init__(self, module, debug):
        self.lexer = lex.lex(module=module,debug=debug)
        self.lexer.prev_ind = 0
        self.lexer.cur_ind = 0
        self.lexer.block_count = 0
        self.lexer.prepend = []
        self.lexer.blanks = []

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        tok = self.lexer.token()

        if tok is None and self.lexer.block_count > 0:
            """
            if end of input with open blocks remaining,
            close the remaining blocks
            """
            tok = lex.LexToken()
            tok.type = 'ENDBLOCK'
            tok.value = None
            tok.lineno = self.lexer.lineno
            tok.lexpos = self.lexer.lexpos
            self.lexer.prepend.extend([tok]*self.lexer.block_count)
            self.lexer.prepend.extend(self.lexer.blanks)
            self.lexer.blanks = []
            self.lexer.block_count = 0
        else:
            self.lexer.prepend.append(tok)

        if len(self.lexer.prepend) > 0:
            return self.lexer.prepend.pop(0)
        return None
