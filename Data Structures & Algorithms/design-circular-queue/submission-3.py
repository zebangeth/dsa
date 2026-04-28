class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.k = k
        self.front = 0
        self.back = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.back] = value
        self.back = (self.back + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.back - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k