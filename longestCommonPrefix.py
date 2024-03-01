
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        first = strs[0]
        p = 0
        while p < len(first):
            match = True
            i = 1
            while i < len(strs):
                if(p < len(strs[i])):
                    match = match and first[p] == strs[i][p]
                else:
                    match = False
                i += 1
            if (match):
                prefix += first[p]
            else:
                break
            p += 1
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["flower","flow","floght"]))
print(solution.longestCommonPrefix(["dog","racecar","floght"]))
print(solution.longestCommonPrefix(["dog"]))
print(solution.longestCommonPrefix(["ab","a"]))
print(solution.longestCommonPrefix(["cir","car"]))