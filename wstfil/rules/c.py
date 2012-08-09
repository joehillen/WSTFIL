tokens = (
    'INDENT',
    'MACRO',
    'STUFF',
    'NL'
)

from wstfil.rules.lex.newline import t_NL
from wstfil.rules.lex.indent import t_INDENT
from wstfil.rules.lex.base import t_error,t_ignore

t_MACRO = r'\#\w+[^\n]+'

t_STUFF = r'[^\n]+'

