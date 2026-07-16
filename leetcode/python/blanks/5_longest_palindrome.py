class Solution:
    def __init__(self):
        self.longest_length = 0
        self.memo = dict()
    def isPalindrome(self, s: str) -> bool:
        # print(f"Module <isPalindrome>: s: {s}: {type(s)}, s[::-1]: {s[::-1]}: {type(s)}, pass: {s == s[::-1] and s != ""}")
        if s not in ["", None] and s[::-1] not in ["", None]: return s == s[::-1]
        else: return False
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s) and len(s) > self.longest_length: return s
        self.longestPalindrome(s[:-1])
        self.longestPalindrome(s[1:])
        self.longestPalindrome(s[1:-1])
        # # case 1: slicing from right
        # for i in range(1, len(s) + 1):
        #     cur_str = s[:i] if s[:i] else None
        #     cur_another_str = s[i:len(s)] if s[i:len(s)] else None
        #     print(f"block 1, i: {i}, s[0:i]: {cur_str} || s[i:{len(s)}]: {cur_another_str}")
        #     # we check by decreasing to find immediate max
        #     if self.isPalindrome(cur_another_str) and len(cur_another_str) > self.longest_length:
        #         print(f"block 1, pal found: s[{i}:{len(s)}], {cur_another_str}")
        #         self.longest_length = len(cur_another_str)
        #         self.answer = cur_another_str
        #         break
        # # case 2: slicing from left
        # for i in range(len(s), 0, -1):
        #     cur_str = s[0:i]
        #     cur_another_str = s[i:len(s)] if s[i:len(s)] else None
        #     print(f"block 2, i: {i}, s[0:{i}]: {cur_str} || s[{i}:{len(s)}]: {cur_another_str}")
        #     # we check by decreasing to find immediate max
        #     if self.isPalindrome(cur_str) and len(cur_str) > self.longest_length:
        #         print(f"block 1, pal found: s[0:{i}], {cur_str}")
        #         self.longest_length = len(cur_str)
        #         self.answer = cur_str
        #         break
            
        # # case 3: slicing from both sides
        # for i in range(0, len(s) - 2):
        #     cur_str = s[i:len(s) - i] if s[i:len(s) - i] else None
        #     print(f"block 3, i: {i} || s[{i}:{len(s) - i}]: {cur_str}")
        #     # we check by decreasing to find immediate max
        #     if self.isPalindrome(cur_str) and len(cur_str) > self.longest_length:
        #         print(f"block 1, pal found: s[0:{i}], {cur_str}")
        #         self.longest_length = len(cur_str)
        #         self.answer = cur_str
        #         break
        return self.answer