class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        A = {}
        l = 0
        maxL = 0

        for r in range(len(s)):
            if s[r] in A:
                l = max(A[s[r]] + 1, l)
            A[s[r]] = r

            maxL = max(r - l + 1, maxL)
        return maxL
