# 作者：Alex
# 2024/10/24 09:08
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = len(s)
        final_result = ""

        def length_str(min_num, max_num):
            while min_num >= 0 and max_num < max_str and s[min_num] == s[max_num]:
                min_num -= 1
                max_num += 1
            return s[min_num + 1: max_num]

        for i in range(max_str):
            result1 = length_str(i, i)
            result2 = length_str(i, i + 1)

            if len(result1) > len(final_result):
                final_result = result1
            if len(result2) > len(final_result):
                final_result = result2

        return final_result