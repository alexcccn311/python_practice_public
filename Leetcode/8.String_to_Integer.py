# 作者：Alex
# 2024/10/27 04:12
"""class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        result_str = ''
        controller = 0
        for i in range(len(s)):
            a = s[i]
            if a == ' ':
                break
            elif a == '+' or a == '-':
                if controller == 0:
                    result_str += a
                    controller = 1
                else:
                    break
            elif a == '0':
                if controller == 3:
                    result_str += a
                else:
                    controller = 2
            elif '1' <= a <= '9':
                result_str += a
                controller = 3
            else:
                break
        if result_str == '' or result_str in ['+', '-']:
            return 0
        result = int(result_str)
        if result < - 2**31: result = - 2**31
        elif result > 2 **31 -1: result = 2 **31 -1
        return result"""


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == "-" else 1
        s = s[1:] if s[0] in {'+', '-'} else s
        result_str = ''
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        s = s.lstrip('0')
        for c in s:
            if not c.isdecimal():
                break
            result_str += c
            if len(result_str) > 10:
                return MAX_INT if sign == 1 else MIN_INT

        if result_str == '':
            return 0
        result = sign * int(result_str)
        return max(MIN_INT, min(result, MAX_INT))

