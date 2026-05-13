class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = collections.deque()
        while columnNumber > 26:
            res.appendleft(columnNumber % 26)
            columnNumber //= 26
        res.appendleft(columnNumber)
        
        for i in range(len(res)):
            res[i] = chr(res[i] + ord('A') - 1)
        
        return "".join(res)
