class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        notval = []
        for num in nums:
            if num != val: notval.append(num)
        nums.clear()
        for num in notval:
            nums.append(num)
        return len(nums)