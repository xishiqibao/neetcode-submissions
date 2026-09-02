class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            maxLen = max(r - l + 1, maxLen)
        return maxLen