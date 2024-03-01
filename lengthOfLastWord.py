class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        foundLastWord = False
        for i in range(len(s)-1, -1, -1):
            if (s[i] == ' '):
                if (foundLastWord):
                    break
            else:
                result += 1
                foundLastWord = True
        return result


solution = Solution()
print(solution.lengthOfLastWord("hello world"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
print(solution.lengthOfLastWord(""))
print(solution.lengthOfLastWord(" "))
print(solution.lengthOfLastWord("                 "))
print(solution.lengthOfLastWord("a  "))
print(solution.lengthOfLastWord("a                 aa"))
print(solution.lengthOfLastWord("a            abc     "))
print(solution.lengthOfLastWord("a            abc   a  "))
