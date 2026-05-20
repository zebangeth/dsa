class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []
        cur_str = ""
        cur_num = 0
        
        for c in s:
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c.isalpha():
                cur_str += c
            elif c == '[':
                str_stack.append(cur_str)
                num_stack.append(cur_num)
                cur_str = ""
                cur_num = 0
            elif c == ']':
                last_str = str_stack.pop()
                last_num = num_stack.pop()
                cur_str = last_str + last_num * cur_str
            else:
                raise ValueError('Invalid character in input')
        
        return cur_str