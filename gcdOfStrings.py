from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # print(str1,str2)
        if(len(str1) < len(str2)):
            return self.gcdOfStrings(str2,str1)
        if(str1 == str2):
            return str2
        if(len(str2) == 0):
            return ""
        if(str1.startswith(str2)):
            return self.gcdOfStrings(str1[len(str2):] ,str2)
        return ""
    

s = Solution()
print(s.gcdOfStrings("ABAB", "ABABAB"))
print(s.gcdOfStrings("ABC", "ABCABC"))
print(s.gcdOfStrings("LEET", "CODE"))
print(s.gcdOfStrings("A", "AAAB"))
print(s.gcdOfStrings("A", "AAAAAA"))
print(s.gcdOfStrings("AA", "AAAAAA"))
print(s.gcdOfStrings("AA", "AAAAA"))
print(s.gcdOfStrings("AAAAAAAAAAAAAAAAAA", "AAACCCAAAAAA"))