class Lexer:
    def __init__(self, text = ""):
        self.text = text
        self.pos = -1
        self.current = None
        self.tokens = []
        self.move()

    def input(self, text):
        self.text = text
        self.pos = -1
        self.current = None
        self.tokens = []
        self.move()

    def move(self):
        self.pos += 1

        try:
            self.current = self.text[self.pos]

        except:
            self.current = None

    def lex(self):
        while self.current != None:
            if self.current == " " or self.current == "\n":
                self.move()

            elif self.current in ".0123456789":
                self.tokens.append(self.get_number())

            elif self.current == "+":
                self.tokens.append("PLUS")
                self.move()

            elif self.current == "-":
                self.tokens.append("MINUS")
                self.move()

            elif self.current == "*":
                self.tokens.append("MULTIPLY")
                self.move()

            elif self.current == "/":
                self.tokens.append("DIVIDE")
                self.move()

            elif self.current == "(":
                self.tokens.append("LPAREN"),
                self.move()

            elif self.current == ")":
                self.tokens.append("RPAREN")
                self.move()

            else:
                raise Exception(f"Illegal Character '{self.current}'")

        return self.tokens

    def get_number(self):
        number = self.current
        dot = 0
        self.move()

        while self.current != None and self.current in ".0123456789":
            if self.current == ".":
                dot += 1

                if dot > 1:
                    break
        
            number += self.current
            self.move()

        if number.startswith("."):
            number = "0" + number

        if number.endswith("."):
            number = number + "0"

        if dot == 0:
            return int(number)

        else:
            return float(number)