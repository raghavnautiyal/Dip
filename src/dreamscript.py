# IMPORTS

from string_with_arrows import *
import string 
import os
import math
import random
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

# Assigning Builtin Functions

BuiltInFunction.print       = BuiltInFunction("print")
BuiltInFunction.input       = BuiltInFunction("input")
BuiltInFunction.input_integer   = BuiltInFunction("input_integer")
BuiltInFunction.clear       = BuiltInFunction("clear")
BuiltInFunction.is_number   = BuiltInFunction("is_number")
BuiltInFunction.is_string   = BuiltInFunction("is_string")
BuiltInFunction.is_list     = BuiltInFunction("is_list")
BuiltInFunction.is_function = BuiltInFunction("is_function")
BuiltInFunction.append      = BuiltInFunction("append")
BuiltInFunction.sin      = BuiltInFunction("sin")
BuiltInFunction.cos      = BuiltInFunction("cos")
BuiltInFunction.tan      = BuiltInFunction("tan")
BuiltInFunction.pop         = BuiltInFunction("pop")
BuiltInFunction.extend      = BuiltInFunction("extend")
BuiltInFunction.len         = BuiltInFunction("len")
BuiltInFunction.run      = BuiltInFunction("run")
BuiltInFunction.say      = BuiltInFunction("say")
BuiltInFunction.root      = BuiltInFunction("root")
BuiltInFunction.randint      = BuiltInFunction("randint")
BuiltInFunction.exitprompt      = BuiltInFunction("exitprompt")
BuiltInFunction.import_      = BuiltInFunction("import_")
BuiltInFunction.to_int     = BuiltInFunction("to_int")
BuiltInFunction.to_float    = BuiltInFunction("to_float")
BuiltInFunction.to_string      = BuiltInFunction("to_string")
BuiltInFunction.reverse      = BuiltInFunction("reverse")
BuiltInFunction.opentab      = BuiltInFunction("opentab")


#######################################
# RUN
#######################################

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("pi", Number.math_pi)
global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("sin", BuiltInFunction.sin)
global_symbol_table.set("cos", BuiltInFunction.cos)
global_symbol_table.set("tan", BuiltInFunction.tan)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("input_integer", BuiltInFunction.input_integer)
global_symbol_table.set("clear", BuiltInFunction.clear)
global_symbol_table.set("cls", BuiltInFunction.clear)
global_symbol_table.set("is_number", BuiltInFunction.is_number)
global_symbol_table.set("is_string", BuiltInFunction.is_string)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_function", BuiltInFunction.is_function)
global_symbol_table.set("add", BuiltInFunction.append)
global_symbol_table.set("remove", BuiltInFunction.pop)
global_symbol_table.set("join", BuiltInFunction.extend)
global_symbol_table.set("length", BuiltInFunction.len)
global_symbol_table.set("run", BuiltInFunction.run)
global_symbol_table.set("say", BuiltInFunction.say)
global_symbol_table.set("root", BuiltInFunction.root)
global_symbol_table.set("random_int", BuiltInFunction.randint)
global_symbol_table.set("exit", BuiltInFunction.exitprompt)
global_symbol_table.set("include", BuiltInFunction.import_)
global_symbol_table.set("integer", BuiltInFunction.to_int)
global_symbol_table.set("decimal", BuiltInFunction.to_float)
global_symbol_table.set("string", BuiltInFunction.to_string)
global_symbol_table.set("reverse", BuiltInFunction.reverse)
global_symbol_table.set("open", BuiltInFunction.opentab)


def run(fn, text):
        # Generate tokens
        lexer = Lexer(fn, text)
        tokens, error = lexer.make_tokens()
        if error: return None, error
        
        # Generate AST
        parser = Parser(tokens)
        ast = parser.parse()
        if ast.error: return None, ast.error

        # Run program
        interpreter = Interpreter()
        context = Context('<dreamscript program>')
        context.symbol_table = global_symbol_table
        result = interpreter.visit(ast.node, context)

        return result.value, result.error