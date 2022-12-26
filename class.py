class Parent:
    def __init__(self, a, b):
        self.num = a
        self.str = b

    def hello(self):
        print("hello")


class Child(Parent):
    def bye(self):  # dead line
        print("good bye")
