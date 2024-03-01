class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if (c == '('):
                stk.append('(')
            elif (c == '{'):
                stk.append('{')
            elif (c == '['):
                stk.append('[')
            elif (c == ')'):
                if (len(stk) < 1 or stk[-1] != '('):
                    return False
                if (stk[-1] == '('):
                    stk.pop()
            elif (c == '}'):
                if (len(stk) < 1 or stk[-1] != '{'):
                    return False
                if (stk[-1] == '{'):
                    stk.pop()
            elif (c == ']'):
                if (len(stk) < 1 or stk[-1] != '['):
                    return False
                if (stk[-1] == '['):
                    stk.pop()
        return len(stk) == 0


solution = Solution()
print(solution.isValid("(])"))
print(solution.isValid(")"))
print(solution.isValid("(){}"))
print(solution.isValid("(){}[]"))
print(solution.isValid("("))
print(solution.isValid("({})"))
print(solution.isValid("({[]})"))
print(solution.isValid("(]"))
