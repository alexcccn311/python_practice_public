class Solution:
    def reverse(self, x: int) -> int:
        x_str= str(abs(x))
        reverse_x = x_str[::-1]
        result = int(reverse_x)
        if x < 0:
            result = -result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result