class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        j = 0
        while True:
            if (i < len(word1)):
                result += word1[i]
                i += 1
            if(j < len(word2)):
                result += word2[j]
                j+=1
            if(i == len(word1) and j == len(word2)):
                break
        return result


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
print(s.mergeAlternately("a", "pqrs"))
print(s.mergeAlternately("a", "p"))
print(s.mergeAlternately("ab", "p"))
print(s.mergeAlternately("abc", "p"))
print(s.mergeAlternately("abcd", "pq"))