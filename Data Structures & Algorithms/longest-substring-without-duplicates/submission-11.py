class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        A = set()
        l = 0
        maxL = 0

        for r in range(len(s)):
            while s[r] in A:
                A.remove(s[l])
                l += 1
            A.add(s[r])
            maxL = max(r - l + 1, maxL)
        return maxL
