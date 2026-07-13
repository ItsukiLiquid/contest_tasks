class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        nums_count = nums.count(target)
        if nums_count == 0: return [-1, -1]
        elif nums_count == 1: return [nums.index(target), nums.index(target)]
        else: return [nums.index(target), nums.index(target) + nums_count - 1]


s = Solution()
nums = [5,7,7,7,8,8,10]
target = 7
print(s.searchRange(nums, target))
        