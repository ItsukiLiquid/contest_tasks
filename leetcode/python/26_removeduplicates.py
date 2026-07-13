class Solution:
    def removeDuplicates(self, nums: list) -> int:
        unique = set(nums)
        nums.clear()
        for num in unique:
            nums.append(num)
        nums.sort()
        return len(nums)
    
a = Solution()
print(a.removeDuplicates([1,1,2]))