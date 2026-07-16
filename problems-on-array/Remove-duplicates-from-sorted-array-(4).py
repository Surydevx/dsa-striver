class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for w in range(len(nums)-1):

            if nums[w] != nums[w+1]:
                numms[k] = nums[w+1]
                k += 1
            else:
                pass
        return k
