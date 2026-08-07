class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        for i in range(len(str(x)) // 2):
            if str(x)[i] != str(x)[len(str(x)) - 1 - i]:
                return False
        return True