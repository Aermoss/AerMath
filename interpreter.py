class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        return node.eval()