import ply.yacc as yacc

tokens = (
    'INDENT',
    'STUFF',
    'MACRO',
    'BLOCK',
    'ENDBLOCK',
    'NL'
)

from wstfil.rules.lex.base import t_error,t_ignore

def t_NL(t):
    r'\n+(?:[ \t]*\n+)*'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.cur_ind = 0
    return t

def t_INDENT(t):
    r'\ \ \ \ '
    if t.lexer.prev_ind <= 0 and t.lexer.cur_ind <= 0:
        t.lexer.prev_ind = 1
        t.lexer.cur_ind  = 1
        t.lexer.block_count += 1
        t.type = 'BLOCK'
        return t
    t.lexer.cur_ind += 1
    if t.lexer.prev_ind < t.lexer.cur_ind:
        t.lexer.prev_ind = t.lexer.cur_ind
        t.lexer.block_count += 1
        t.type = 'BLOCK'
        return t


def t_STUFF(t):
    r'[^\#\ \n\t]+[^\n]*'
    if t.lexer.prev_ind > 0 and t.lexer.prev_ind > t.lexer.cur_ind:
        t.lexer.prev_ind = t.lexer.cur_ind
        t.lexer.block_count -= 1
        t.type = 'ENDBLOCK'
    return t    

t_MACRO = r'[ \t]*\#\w+[^\n]+'

def p_exps(p):
    'exps : exps exp'
    p[0] = p[1]+[p[2]]

def p_exps_end(p):
    'exps : exp'
    p[0] = [p[1]]

def p_exp(p):
    '''
    exp : echo
        | block
        | line
    '''
    p[0] = p[1]

def p_block(p):
    'block : BLOCK exps ENDBLOCK'
    p[0] = ('block',p[1],p[2])


def p_echo_macro(p):
    'echo : MACRO NL'
    p[0] = ('echo',p[1]+p[2])

def p_line(p):
    'line : STUFF NL'
    p[0] = ('line',p[1],p[2])

parser = yacc.yacc()
