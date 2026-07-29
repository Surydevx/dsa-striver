"""class Solution:
    def moveZeroes(self, nums):
        my_zeroes = []
        for w in range(len(nums)):
            if nums[w] ==0:
                my_zeroes.append(w)
        for w in reversed(my_zeroes):
            del nums[w]
        counter = len(my_zeroes)
        while counter:
            nums.append(0)
            counter -= 1"""
            # first solution 
# let's do better.
"""class Solution:
    def moveZeroes(self, nums):
        non_zeroes = []
        counter = 0
        for w in nums:
            if w != 0:
                non_zeroes.append(w)
            elif w == 0 :
                counter +=1
        non_zeroes = non_zeroes[:] + [0] * counter
        for w in range(len(nums)):
            nums[w]  = non_zeroes[w]"""
# second solution
# let's do even better
class Solution:
    
    def moveZeroes(self, nums):
        # overwrite the zeroes with the next non zero number in array.
        index = 0  # points to the index of valid position for non_zeores.
        for w in range(len(nums)):
            if nums[w] != 0:
                nums[w], nums[index] = nums[index],  nums[w]
                index += 1
# got the optimum solution on third try.  :) yayyyyyyy!
