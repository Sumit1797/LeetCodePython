class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        stack = []
        for i in s:
            if (i == '(' or i == '[' or i == '{'):
                stack.append(i)
            else:
                if(len(stack) > 0):
                    char = stack[-1]
                    if ((char == '(' and i != ')')or (char == '[' and i != ']') or (char == '{' and i != '}') ):
                        return False
                    del stack[len(stack) - 1]
                else:
                    return False
        if len(stack) > 0:
            return False        
        return True