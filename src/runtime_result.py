from parser import *
from tokens import *
from nodes import *
from lexer import *
from data_types import *
from interpreter import *
from symbol_table import *
from context import * 
from runtime_result import *
from position import *

# Runtime Result

class RTResult:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False

    
    def register(self, res):
        self.error = res.error
        self.func_return_value = res.func_return_value
        self.loop_should_break = res.loop_should_break
        self.loop_should_continue = res.loop_should_continue
        return res.value

    def success(self, value):
        self.reset()
        self.value = value
        return self
        
    def success_return(self, value):
        self.reset()
        self.func_return_value = value
        return self
    
    def success_continue(self):
        self.reset()
        self.loop_should_continue = True
        return self
    
    def success_break(self):
        self.reset()
        self.loop_should_break = True
        return self


    def failure(self, error):
        self.reset()
        self.error = error
        return self
        
    def should_return(self):
        return (
            self.error or
            self.func_return_value or
            self.loop_should_continue or
            self.loop_should_break
    )
