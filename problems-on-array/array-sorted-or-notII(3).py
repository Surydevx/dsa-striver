class Solution:
    def isSorted(self, nums):
        x = 1
        for w in range(len(nums)-1):
            if nums[w] > nums[w+1]:
                x = 0
            else:
                pass
        return bool(x)
