class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        return True if str1 == str2 else False