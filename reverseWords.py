class Solution:
    def reverseWords(self, s: str) -> str:
        # splits = s.split(" ")
        # splits = [i for i in splits if i!='']
        # splits.reverse()
        # return " ".join(splits)
        return " ".join(s.split()[::-1])
        
        
s = Solution()
print(s.reverseWords("hello world"))
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
