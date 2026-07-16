# btw i can solve this in one line using the deque method called rotate(), anyways let's do something beddarr.
class Solution:
    def rotateArray(self, nums, k: int) -> None:
    # how about we use a for loop to remove elements from front and shovig them at the end?
        # while k:
            # nums.append(nums.pop(0))
            # k -= 1
# well i hope the solution could end here but NO!, actually we are goingto do some maths..
        counter = k % len(nums) # this returns the remiander handling all three cases when k>len(nums), k<len(nums) and k = len(nums)
        while counter:
            nums.append(nums.pop(0))
            counter -= 1
# easy peasy.
# one even better solution i came to see eas suing slicing approach and usingthe concept of nums = nums[counter:]+ nums[:counter], and this returnns a rotated nums list and where counter = k % len(nums)

