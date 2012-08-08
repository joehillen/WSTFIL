tokens = (
    'MACRO',
    'STUFF',
    'INDENT',
    'NL'
)

from wstfil.rules.lex.newline import t_NL
from wstfil.rules.lex.indent import t_INDENT
from wstfil.rules.lex.base import t_error,t_ignore

def t_MACRO(t):
    r'\#\w+[^\n]+'

def t_STUFF(t):
    r'[^\n]+'

