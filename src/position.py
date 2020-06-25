from parser import *
from nodes import *
from lexer import *
from data_types import *
from interpreter import *
from symbol_table import *
from context import *    
from runtime_result import *


class Position:
        def __init__(self, idx, ln, col, fn, ftxt):
                self.idx = idx
                self.ln = ln
                self.col = col
                self.fn = fn
                self.ftxt = ftxt

        def advance(self, current_char=None):
                self.idx += 1
                self.col += 1

                if current_char == '\n':
                        self.ln += 1
                        self.col = 0

                return self

        def copy(self):
                return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

     