class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            number = s[i]
            nextNumber = ' '
            if (i < len(s) - 1):
                nextNumber = s[i+1]
            if (number == 'I'):
                if (nextNumber == 'V'):
                    result += 4
                    i += 1
                elif (nextNumber == 'X'):
                    result += 9
                    i += 1
                else:
                    result += 1
            elif (number == 'V'):
                result += 5
            elif (number == 'X'):
                if (nextNumber == 'L'):
                    result += 40
                    i += 1
                elif (nextNumber == 'C'):
                    result += 90
                    i += 1
                else:
                    result += 10
            elif (number == 'L'):
                result += 50
            elif (number == 'C'):
                if (nextNumber == 'D'):
                    result += 400
                    i += 1
                elif (nextNumber == 'M'):
                    result += 900
                    i += 1
                else:
                    result += 100
            elif (number == 'D'):
                result += 500
            elif (number == 'M'):
                result += 1000
            i+=1
        return result


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("IV"))
print(solution.romanToInt("IX"))
print(solution.romanToInt("X"))
print(solution.romanToInt("XXVII"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))