class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, base = 2) + int(b, base = 2)))[2:]
        
x = Solution()
print(x.addBinary("11", "1"), type(x.addBinary("11", "1")))