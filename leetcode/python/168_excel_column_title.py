class Solution:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def convertToTitle(self, columnNumber: int) -> str:
        # we need to write columnNumber as linear combination of 26
        # colNumber = a * 26^n + b * 26^(n - 1) + c * 26 ^ (n - 2) .... + C
        result = ""
        if columnNumber == 1: return "A"
        while columnNumber > 0:
            columnNumber -= 1
            print(f"CN: {columnNumber}")
            result = result + self.alphabet[columnNumber % 26]
            columnNumber //= 26
        return result[::-1]
