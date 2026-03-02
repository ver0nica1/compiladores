import ply.lex as lex

# Tokens

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Expresiones regulares

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Error léxico:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Main

if __name__ == '__main__':
    while True:
        try:
            data = input("expr > ")
        except EOFError:
            break

        lexer.input(data)

        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)