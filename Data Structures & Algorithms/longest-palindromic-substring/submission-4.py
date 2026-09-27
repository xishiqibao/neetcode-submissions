class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        maxLen = 1

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if(length <= 3):
                        dp[i][j] = True
                    elif(dp[i + 1][j - 1]):
                        dp[i][j] = True
                if(dp[i][j]):
                    start = i
                    maxLen = length

        return s[start : start + maxLen]