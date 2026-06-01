class Solution:
    def decodeString(self, s: str) -> str:
        str_stack, num_stack = [], []
        cur_str, cur_num = "", 0
        for c in s:
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c.isalpha():
                cur_str += c
            elif c == '[':
                str_stack.append(cur_str)
                num_stack.append(cur_num)
                cur_str, cur_num = "", 0
            elif c == ']':
                num = num_stack.pop()
                cur_str *= num
                cur_str = str_stack.pop() + cur_str
            else:
                raise ValueError("invalid char in the input s")

        return cur_str

# str_stack = [a]
# num_stack = [2]
# cur_str = bbb
# cur_num = 