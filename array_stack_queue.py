class Array:
    def __init__(self, size):
        self.data = [None] * size

    def insert(self, index, value):
        self.data[index] = value

    def delete(self, index):
        self.data[index] = None

    def access(self, index):
        return self.data[index]
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0
