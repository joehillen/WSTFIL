def t_NL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
