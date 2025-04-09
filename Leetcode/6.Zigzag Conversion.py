# 作者：Alex
# 2024/10/25 19:30
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        final_str = ''
        for times in range(0, len(s), 2 * numRows - 2):
            final_str += s[times]

        row = 2
        times = 0
        while row < numRows:
            if times % 2 == 0:
                location = (row - 1) + (times // 2) * (2 * numRows - 2)
            else:
                location = (2 * numRows - row - 1) + (times // 2) * (2 * numRows - 2)
            if location >= len(s):
                times = 0
                row += 1
                continue
            final_str += s[location]
            times += 1

        for times in range(numRows - 1, len(s), 2 * numRows - 2):
            final_str += s[times]
        return final_str

