import math
class Solution:
    def ctoi(self, c: str) -> int: # char
        return ord(c) - ord("0")
    def stoi(self, s: str) -> int: # string to integer, c++ reference
        result = 0
        for i in range(0, len(s)): # s[0] -> 6, s[1] -> 7, 10^(len(s) - i - 1)
            result += math.pow(10, len(s) - i - 1) * self.ctoi(s[i])
        return result
    def multiply(self, num1: str, num2: str) -> str:
        result = ""
        intnum1 = intnum2 = 0
        if num1 == 0 or num2 == 0: return "0"
        elif num1 == 1 or num2 == 1: return num1 if num2 == "1" else num2
        else:
            return str(self.stoi(num1) * self.stoi(num2))
            

x = Solution()
print(x.stoi("67"), type(x.stoi("67")))
print(x.multiply("123456789", "987654321"), type(x.multiply("123456789", "987654321")))

n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(n))