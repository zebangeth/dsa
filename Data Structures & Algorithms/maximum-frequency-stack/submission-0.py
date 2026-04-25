class FreqStack:

    def __init__(self):
        self.count_stack = collections.defaultdict(list)
        self.val_count = collections.defaultdict(int)
        self.max_count = 0

    def push(self, val: int) -> None:
        cur_count = self.val_count[val]
        self.count_stack[cur_count + 1].append(val)
        self.val_count[val] += 1
        self.max_count = max(cur_count + 1, self.max_count)
        
    def pop(self) -> int:
        popped = self.count_stack[self.max_count].pop()
        self.val_count[popped] -= 1
        if not self.count_stack[self.max_count]:
            self.count_stack.pop(self.max_count)
            self.max_count -= 1
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()