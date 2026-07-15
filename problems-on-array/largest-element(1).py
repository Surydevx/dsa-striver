class Solution:
    def largestElement(self, nums):
        for w in range(len(nums)-1):
                if nums[0]< nums[w+1]:
                    nums[0],nums[w+1] = nums[w+1],nums[0]
        return nums[0] 
