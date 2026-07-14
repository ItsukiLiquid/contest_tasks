class Solution:
    def safeIsInstanceInt(self, s: str) -> bool:
        ASCIIrnge = ord(s) - ord("0")
        # print(ASCIIrnge)
        return ASCIIrnge <= 9 and ASCIIrnge >= 0
    def myAtoi(self, s: str) -> int:
        while True:
            try:
                result = int(s)
                if isinstance(result, int): return max(min(result, 2**31 - 1), -2**31)
            except ValueError:
                if len(s[:-1]) > 0: return self.myAtoi(s[:-1])
                elif len(s[:-1]) == 0: return 0
        
        # result = ""
        # try:
        #     return int(s)
        # except ValueError:
        #     result = ""
        #     pivotZero = True
        #     signDetected = False
        #     amplifier = 1 
        #     for i in range(len(s)):
        #         if s[i] == " ":
        #             print(f"i: {i}, part: if")
        #         elif s[i] == "-" and not signDetected:
        #             print(f"i: {i}, s[i] = {s[i]}, part: s[i] == '-', result: {result}")
        #             amplifier = -1
        #             signDetected = True
        #         # elif s[i] == "0" and pivotZero:
        #         #     print(f"i: {i}, s[i] = {s[i]}, part: s[i] == '0', result: {result}")
        #         #     pivotZero = False
        #         else:
        #             if self.safeIsInstanceInt(s[i]):
        #                 signDetected = True
        #                 result = result + s[i]
        #                 print(f"i: {i}, s[i] = {s[i]}, part: s[i] is integer, result: {result} ")
        #             elif not result: return 0
        #             else:
        #                 print(f"i: {i}, s[i] = {s[i]}, part: s[i] = is not integer, result: {result}")
        #                 return max(min(int(result) * amplifier, 2**31 - 1), -2**31)
