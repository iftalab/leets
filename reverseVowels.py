class Solution:
    def isVowel(self, c: chr) -> chr:
        lc = c.lower()
        return lc.lower() == 'a' or lc.lower() == 'e' or lc.lower() == 'i' or lc.lower() == 'o' or lc.lower() == 'u'
        
    def reverseVowels(self, s: str) -> str:
        data = list(s)
        vowels = []
        for c in data:
            if(self.isVowel(c)):
                vowels.append(c)
        vowels.reverse()
        if(len(vowels) == 0):
            return s
        j = 0
        for i in range(0, len(data)):
            if(self.isVowel(data[i])):
                data[i] = vowels[j]
                j+=1
        return "".join(data)
        
s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leet code"))
print(s.reverseVowels("aeiou"))
print(s.reverseVowels("aeioU"))
print(s.reverseVowels("klmn"))
print(s.reverseVowels("k"))
print(s.reverseVowels("o"))
print(s.reverseVowels("klmno"))
    