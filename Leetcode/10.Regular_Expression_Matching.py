# 作者：Alex
# 2024/10/28 12:49
"""import re

def is_match(s,p):
    return bool(re.match(p,s))

if __name__ == '__main__':
    s = "aa"
    p = ".*"
    print(is_match(s,p))"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # 缓存中间结果

        def dp(i, j):
            """返回 s[i:] 是否匹配 p[j:]"""
            if (i, j) in memo:  # 检查缓存，避免重复计算
                return memo[(i, j)]

            if j == len(p):  # 模式用完了，检查字符串是否也用完
                return i == len(s)

            # 检查当前字符是否匹配（包括 '.' 通配符）
            first_match = i < len(s) and p[j] in {s[i], '.'}

            if j + 1 < len(p) and p[j + 1] == '*':
                # 两种情况：
                # 1. '*' 匹配 0 次：跳过当前字符和 '*'
                # 2. '*' 匹配 1 次或更多：匹配当前字符，并递归检查剩余部分
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # 常规匹配，递归检查剩余部分
                memo[(i, j)] = first_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        return dp(0, 0)  # 从字符串和模式的开头开始匹配

"""