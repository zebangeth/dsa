class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        pop_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return pop_val
        

    def top(self) -> int:
        if not self.q1:
            return None
        return self.q1[-1]
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()