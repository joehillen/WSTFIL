import ply.yacc as yacc

tokens = (
    'INDENT',
    'STUFF',
    'MACRO',
    'NL'
)

from wstfil.rules.lex.newline import t_NL
from wstfil.rules.lex.indent import t_INDENT
from wstfil.rules.lex.base import t_error,t_ignore

t_STUFF = r'[^\#\ \n\t]+[^\n]*'
t_MACRO = r'\#\w+[^\n]+'

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
    'block : line indented '
    p[0] = ('block',p[1],p[2])

def p_indented(p):
    '''indented : indented INDENT exp'''
    p[0] = p[1] + [p[3]]

def p_indented_last(p):
    'indented : INDENT exp'
    p[0] = [p[2]]

def p_echo_macro(p):
    'echo : MACRO NL'
    p[0] = ('echo',p[1]+p[2])

def p_line(p):
    'line : STUFF NL'
    p[0] = ('line',p[1],p[2])

parser = yacc.yacc()
