class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.array = [None] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.array[self.rear] = value
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.array[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.array[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
