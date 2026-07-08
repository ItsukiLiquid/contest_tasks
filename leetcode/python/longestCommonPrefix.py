class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        words = list(set(sorted(strs, key=len)))
        if len(words) == 1: return words[0]
        # print(words)
        # print("\n")
        result = ""
        for i in range(0, len(words[0])):
            # print(len(words[0]))
            common_index = 0
            for word in words:
                # print(f"{i}. {word}")
                if word.startswith(words[0][0:i]): common_index += 1
                # print(common_index)
            if common_index == len(words):
                if len(words[0]) == 1: result = words[0][0:i+1]
                else: result = words[0][0:i]
                # print("Yes!")
                # print(words)
        return result


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "fly"]))