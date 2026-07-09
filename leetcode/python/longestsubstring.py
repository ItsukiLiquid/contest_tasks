class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# class Solution():
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = 0
#         for i in range(0, len(s)):
#             for j in range(i + result + 1, len(s) + 1):
#                 # print(f"i: {i}, j: {j}, s[i:j]: {s[i:j]}")
#                 if len(s[i:j]) == len(set(s[i:j])) and len(s[i:j]) > result:
#                     result = len(s[i:j])
#         return result

# # class Solution:
# #     def lengthOfLongestSubstring(self, s: str) -> int:
# #         result = 0
# #         for i in range(0, len(s)):
# #             for j in range(i + result + 1, len(s) + 1):
# #                 # print(f"i: {i}, j: {j}, s[i:j]: {s[i:j]}")
# #                 if len(s[i:j]) == len(set(s[i:j])) and len(s[i:j]) > result:
# #                     result = len(s[i:j])
# #         return result
#         # if len(s) == 1: return 1
#         # elif len(s) == 2:
#         #     if s[0] == s[1]: return 1
#         #     else: return 2
#         # # we take a one letter and put it in list
#         # notRepeatedChars = []
#         # result = 0
#         # for i in range(0, len(s) - 1):
#         #     head = s[i]
#         #     # notRepeatedChars.append(head)
#         #     for j in range(i, len(s)):
#         #         if s[j] not in notRepeatedChars:
#         #             notRepeatedChars.append(s[j])
#         #             # print(f"Not in: {notRepeatedChars}")
#         #         else:
#         #             if result < len(notRepeatedChars): result = len(notRepeatedChars)
#         #             print(f"Clearing: {notRepeatedChars}")
#         #             notRepeatedChars.clear()
#         # # print(f"Final: {notRepeatedChars}")
#         # return
    

# s = Solution()            
# print(s.lengthOfLongestSubstring("pwwkew"))