class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        result = ""
        words = sorted(strs, key=len)
        size = len(words)
        print(words)
        if len(strs) == 1: return strs[0]
        # we check the smallest word, by building up word
        for i in range(1, len(words[0]) + 1):
            result = words[0][0:i]
            print(words[0][0:i])
            for word in words:
                if word[0:i] != result: return result[:-1]
        return result
            
        # words = list(set(sorted(strs, key=len)))
        # if len(words) == 1: return words[0]
        # # print(words)
        # # print("\n")
        # result = ""
        # for i in range(0, len(words[0])):
        #     # print(len(words[0]))
        #     common_index = 0
        #     for word in words:
        #         # print(f"{i}. {word}")
        #         if word.startswith(words[0][0:i]): common_index += 1
        #         # print(common_index)
        #     if common_index == len(words):
        #         if len(words[0]) == 1: result = words[0][0:i+1]
        #         else: result = words[0][0:i]
        #         # print("Yes!")
        #         # print(words)
