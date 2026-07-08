class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if (len(needle) > len(haystack)): return -1
        # we loop through every letter and also check needle
        result = -1
        for i in range(0, len(haystack)):
            # if the first letter of needle is appeared, check for continuity
            if haystack[i] == needle[0]:
                for j in range(0, len(needle)):
                    try:
                        if haystack[i + j] != needle[j]: break # no found, start from shifting
                    except IndexError: return -1
                    if j == len(needle) - 1 and haystack[i + j] == needle[j]: return i
        return result
    
s = Solution()
print(s.strStr("leetcode", "leeto"))
