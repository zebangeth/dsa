class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        result = [0] * (len(num1) + len(num2))
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                idx = i + j + 1
                temp = (result[idx] + int(num1[i]) * int(num2[j]))
                result[idx] = temp % 10
                result[idx - 1] += temp // 10
        if carry:
            result[0] = carry
        return "".join([str(c) for c in result]) if result[0] != 0 else "".join([str(c) for c in result[1:]])
