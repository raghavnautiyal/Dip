from parser import *
from nodes import *
from data_types import *
from interpreter import *
from symbol_table import *
from context import *    
from runtime_result import *
from position import *
import string 

DIGITS = '0123456789'

LETTERS = string.ascii_letters

LETTERS_DIGITS = LETTERS + DIGITS

TT_INT      = 'INT'
TT_FLOAT    = 'FLOAT' 
TT_STRING   = 'STRING'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MODULUS  = 'MODULUS'
TT_POWER    = 'POWER'
TT_EQUALS = 'EQUALS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'
TT_LSQUARE  = 'LSQUARE'
TT_RSQUARE  = 'RSQUARE'
TT_EE       = 'EE'
TT_NE       = 'NE'
TT_LT       = 'LT'
TT_GT       = 'GT'
TT_LTE      = 'LTE'
TT_GTE      = 'GTE'
TT_COMMA    = 'COMMA'
TT_ARROW    = 'ARROW'
TT_NEWLINE  = 'NEWLINE'
TT_EOF      = 'EOF'

KEYWORDS = [
    'variable',
    'and',
    'or',
    'not',
    'if',
    'then',
    'elif',
    'else',
    'for',
    'to',
    'step',
    'while',
    'function',
    'end',
    'continue',
    'return',
    'breakout',
]

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
                self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        return self.type == type_ and self.value == value
        
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


class Lexer:
        def __init__(self, fn, text):
                self.fn = fn
                self.text = text
                self.pos = Position(-1, 0, -1, fn, text)
                self.current_char = None
                self.advance()
        
        def advance(self):
                self.pos.advance(self.current_char)
                self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

        def make_tokens(self):
                tokens = []

                while self.current_char != None:
                        if self.current_char in ' \t':
                                self.advance()
                        elif self.current_char == '#':
                                self.skip_comment()
                        elif self.current_char in DIGITS:
                                tokens.append(self.make_number())
                        elif self.current_char in ';\n':
                                tokens.append(Token(TT_NEWLINE, pos_start=self.pos))
                                self.advance()
                        elif self.current_char in LETTERS:
                            tokens.append(self.make_identifier())
                        elif self.current_char == '+':
                                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '"' :
                            tokens.append(self.make_string())
                        elif self.current_char == '-':
                                tokens.append(self.make_minus_or_arrow())
                        elif self.current_char == '*':
                                tokens.append(Token(TT_MUL, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '/':
                                tokens.append(Token(TT_DIV, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '%':
                                tokens.append(Token(TT_MODULUS, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '^':
                                tokens.append(Token(TT_POWER, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '(':
                                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == ')':
                                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '[':
                                tokens.append(Token(TT_LSQUARE, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == ']':
                                tokens.append(Token(TT_RSQUARE, pos_start=self.pos))
                                self.advance()
                        elif self.current_char == '!':
                            token, error = self.make_not_equals()
                            if error: return[], error
                            tokens.append(token)
                            self.advance()
                        elif self.current_char == '=':
                                tokens.append(self.make_equals())
                                self.advance()
                        elif self.current_char == '<':
                                tokens.append(self.make_less_than())
                                self.advance()
                        elif self.current_char == '>':
                                tokens.append(self.make_greater_than())
                                self.advance()
                        elif self.current_char == ',':
                                tokens.append(Token(TT_COMMA, pos_start=self.pos))
                                self.advance()
                        else:
                                pos_start = self.pos.copy()
                                char = self.current_char
                                self.advance()
                                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

                tokens.append(Token(TT_EOF, pos_start=self.pos))
                return tokens, None

        
        def make_number(self):
                num_str = ''
                dot_count = 0
                pos_start = self.pos.copy()

                while self.current_char != None and self.current_char in DIGITS + '.':
                        if self.current_char == '.':
                                if dot_count == 1: break
                                dot_count += 1
                                num_str += '.'
                        else:
                                num_str += self.current_char
                        self.advance()

                if dot_count == 0:
                        return Token(TT_INT, int(num_str), pos_start, self.pos)
                else:
                        return Token(TT_FLOAT, float(num_str), pos_start, self.pos)

        def make_string(self):
            string = ''
            pos_start = self.pos.copy()
            escape_character = False
            self.advance()

            escape_characters = {
                'n': '\n',
                't': '\t',
            }

            while self.current_char != None and (self.current_char != '"' or escape_character):
                if escape_character:
                    string += escape_characters.get(self.current_char, self.current_char)
                else:
                    if self.current_char == '\\':
                        escape_character = True
                    else:
                        string += self.current_char
                self.advance()
                escape_character = False

            self.advance()
            return Token(TT_STRING, string, pos_start, self.pos)


        def make_identifier(self):
            id_str = ''
            pos_start = self.pos.copy()
            while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
                id_str += self.current_char
                self.advance()

            tok_type = TT_KEYWORD if id_str in KEYWORDS else  TT_IDENTIFIER
            return Token(tok_type, id_str, pos_start, self.pos)

        def make_minus_or_arrow(self):
            tok_type = TT_MINUS
            pos_start = self.pos.copy()
            self.advance()

            if self.current_char == '>':
                self.advance()
                tok_type = TT_ARROW
            
            return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

        def make_not_equals(self):
            pos_start = self.pos.copy()
            self.advance()

            if self.current_char == '=':
                #self.advance()
                return Token(TT_NE, pos_start=pos_start, pos_end=self.pos), None

            self.advance()
            return None, ExpectedCharError(pos_start, self.pos, "'=' (after '!')")

        def make_equals(self):
            tok_type = TT_EQUALS
            pos_start = self.pos.copy()
            self.advance()
            
            if self.current_char == '=':
                #self.advance()
                tok_type = TT_EE
                
            return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

        def make_less_than(self):
            tok_type = TT_LT
            pos_start = self.pos.copy()
            self.advance()

            if self.current_char == '=':
                #self.advance()
                tok_type = TT_LTE

            return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

        def make_greater_than(self):
            tok_type = TT_GT
            pos_start = self.pos.copy()
            self.advance()

            if self.current_char == '=':
                #self.advance()
                tok_type = TT_GTE

            return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

        def skip_comment(self):
            self.advance()

            while self.current_char != '\n':
                self.advance()

            self.advance()
    