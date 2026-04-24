class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in match:
                if not stack or stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)
        return not stack
