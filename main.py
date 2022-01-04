from lexer import *
from parser import *
from interpreter import *

lexer = Lexer()
parser = Parser()
interpreter = Interpreter()

while True:
    text = input("> ")
    lexer.input(text)
    tokens = lexer.lex()
    parser.input(tokens)
    tree = parser.parse()
    value = interpreter.visit(tree)
    print(value)