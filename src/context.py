from parser import *
from tokens import *
from nodes import *
from lexer import *
from data_types import *
from interpreter import *
from symbol_table import *
from runtime_result import *
from position import *

class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None