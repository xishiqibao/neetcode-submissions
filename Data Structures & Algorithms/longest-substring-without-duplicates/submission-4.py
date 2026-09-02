class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if(s[r] in map):
                l = max(map[s[r]] + 1, l)
            map[s[r]] = r
            res = max(r - l + 1, res)
        return res