def t_error(t):
    print "Illegal character '{0}' @ {1},{2}".format(t.value[0],t.lexer.lineno,t.lexer.lexpos)
    t.lexer.skip(1)

t_ignore = ''

