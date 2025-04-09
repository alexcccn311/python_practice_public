# 作者：Alex
# 2024/10/28 12:31
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        str_num = str(x)
        for i in range(len(str_num) // 2):
            if str_num[i] != str_num[-i - 1]:
                return False

        return True

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)[::-1]
        if str(x) == strX:
            return True
        else:
            return False
"""