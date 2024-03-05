class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s == ''):
            return True
        i = 0
        for x in t:
            if x == s[i]:
                i += 1
            if i == len(s):
                return True
        return False
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("ahbgdc", "ab"))
print(s.isSubsequence("", "ab"))
print(s.isSubsequence("a", ""))
print(s.isSubsequence("a", "bbabb"))
print(s.isSubsequence("ac", "bbabbcc"))
print(s.isSubsequence("axc", "ahbgdc"))