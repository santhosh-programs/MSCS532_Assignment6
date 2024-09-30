class Queue:
    def __init__(self, size):
        self._queue = [None] * size
        self._front = -1
        self._rear = -1

    def enqueue(self, value):
        if self._rear < len(self._queue) - 1:
            if self._front == -1:
                self._front = 0
            self._rear += 1
            self._queue[self._rear] = value
        else:
            print("Queue Overflow")

    def dequeue(self):
        if self._front > self._rear or self._front == -1:
            print("Queue Underflow")
            return None
        else:
            value = self._queue[self._front]
            self._queue[self._front] = None
            self._front += 1
            return value

    def peek(self):
        if self._front > self._rear or self._front == -1:
            return None
        else:
            return self._queue[self._front]

    def is_empty(self):
        return self._front == -1 or self._front > self._rear

    def display(self):
        print(self._queue)


class Stack:
    def __init__(self, size):
        self._stack = [None] * size
        self._top = -1

    def push(self, value):
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = value
        else:
            print("Stack Overflow")

    def pop(self):
        if self._top >= 0:
            value = self._stack[self._top]
            self._stack[self._top] = None
            self._top -= 1
            return value
        else:
            print("Stack Underflow")
            return None

    def peek(self):
        if self._top >= 0:
            return self._stack[self._top]
        else:
            return None

    def is_empty(self):
        return self._top == -1

    def display(self):
        print(self._stack)


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print(queue.dequeue())
    print(queue.peek())

    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.display()
    print(stack.pop())
    print(stack.peek())
