# 作者：Alex
# 2024/10/17 05:20
"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = len(s)
        def check_repeating_characters(a):
            b = set()
            c = a
            while True:
                if s[c] not in b:
                    b.add(s[c])
                    c += 1
                else:
                    return (c- a)
                if c== l:
                    return (c- a)
        for i in range(l):
            length = check_repeating_characters(i)
            if length > max_length: max_length = length
        return max_length"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length