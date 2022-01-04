class NumberNode:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

class SubtractNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() - self.right.eval()

class MultiplyNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

class DivideNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() / self.right.eval()

class PlusNode:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.eval()

class MinusNode:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return -self.value.eval()