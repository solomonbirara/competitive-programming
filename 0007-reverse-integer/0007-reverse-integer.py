class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        negative = x < 0
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return 0
            
            result = result * 10 + digit
        
        if negative:
            result = -result
        
        return result if INT_MIN <= result <= INT_MAX else 0
    

        
        