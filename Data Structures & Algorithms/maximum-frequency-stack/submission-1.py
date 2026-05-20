class FreqStack:

    def __init__(self):
        self.max_frq = 0
        # {frq: [val, val, ...], ...}
        self.frq_to_vals = collections.defaultdict(list)
        # {val: frq, val: frq, ...}
        self.val_to_frq = collections.defaultdict(int)

    def push(self, val: int) -> None:
        self.val_to_frq[val] += 1
        self.max_frq = max(self.max_frq, self.val_to_frq[val])
        self.frq_to_vals[self.val_to_frq[val]].append(val)

    def pop(self) -> int:
        val = self.frq_to_vals[self.max_frq].pop()
        self.val_to_frq[val] -= 1
        if not self.frq_to_vals[self.max_frq]:
            self.max_frq -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()