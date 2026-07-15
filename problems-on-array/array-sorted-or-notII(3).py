class Solution:
    def isSorted(self, nums):
        for w in range(len(nums) - 1):
            if nums[w] > nums[w + 1]:
                return False
        return True
