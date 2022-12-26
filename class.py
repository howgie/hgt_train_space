class Parent:
    def __init__(self, a, b):
        self.num = a
        self.str = b

    def hello(self):
        print("hello")


class Child(Parent):
    def bye(self):　#子クラスで新たに定義したメソッド
        print("good bye")