class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        quotient = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            for i in range(31, -1, -1):
                if (divisor << i) <= dividend:
                    dividend -= divisor << i
                    quotient += 1 << i
                    break
        if sign: quotient = -quotient
        
        return max(min(quotient, 2**31-1), -2**31)
    
s = Solution()
print(s.divide(-2147483648, -1))