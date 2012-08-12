def t_NL(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    return t
