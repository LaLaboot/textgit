"""队列的实现"""
class Queue():
    def __init__(self, size):
        self.queue = [0 for _ in range(size)]
        self.rear = 0
        self.front = 0
        self.size = size

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty')

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

if __name__ == "__mian__":
    queue = Queue(10)
    for i in range(9):
        queue.push(i)
    print(queue.queue)
    for i in range(9):
        print(queue.pop())
    print(queue.pop())

