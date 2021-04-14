"""栈的实现"""
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.stack)