from nodes import *

class Parser:
    def __init__(self, tokens = []):
        self.tokens = tokens
        self.pos = -1
        self.current = None
        self.move()

    def error(self):
        raise Exception("Invalid Syntax.")

    def input(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.current = None
        self.move()

    def move(self):
        self.pos += 1

        try:
            self.current = self.tokens[self.pos]

        except:
            self.current = None

    def parse(self):
        if self.current == None:
            return None

        result = self.expr()

        if self.current != None:
            self.error()

        return result

    def expr(self):
        result = self.term()

        while self.current != None and self.current in ["PLUS", "MINUS"]:
            if self.current == "PLUS":
                self.move()
                result = AddNode(result, self.term())

            elif self.current == "MINUS":
                self.move()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current != None and self.current in ["MULTIPLY", "DIVIDE"]:
            if self.current == "MULTIPLY":
                self.move()
                result = MultiplyNode(result, self.factor())

            elif self.current == "DIVIDE":
                self.move()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.current

        if token == "LPAREN":
            self.move()
            result = self.expr()

            if self.current != "RPAREN":
                self.error()

            self.move()
            return result

        if isinstance(token, int) or isinstance(token, float):
            self.move()
            return NumberNode(token)

        elif token == "PLUS":
            self.move()
            return PlusNode(self.factor())

        elif token == "MINUS":
            self.move()
            return MinusNode(self.factor())

        self.error()