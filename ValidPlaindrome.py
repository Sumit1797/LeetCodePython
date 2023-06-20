class Solution:

    def isAlphanumer(c:chr) -> bool:
        if ((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')):
            return True
        return False


    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ''
        for i in s:
            if Solution.isAlphanumer(i):
                newStr += i
        return newStr == newStr[::-1]
