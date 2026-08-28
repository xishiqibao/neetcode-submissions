# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if(len(s) != len(t)):
#             return False
#         str1 = sorted(s)
#         str2 = sorted(t)
#         return str1 == str2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        S, T = {}, {}
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        return S == T


