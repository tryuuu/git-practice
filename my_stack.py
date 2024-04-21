class My_Stack():
    # selfは自分のクラスのインスタンスを指す
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()

if __name__ == '__main__':
    stack = My_Stack()
    print(stack.stack)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(stack.stack)