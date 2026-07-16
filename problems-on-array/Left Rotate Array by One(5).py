class Solution:
    def rotateArrayByOne(self, nums):
        nums.append(nums.pop(0))
## alternative solution using deque.
#from collections import deque
#class solution:
    #def rotateArrayByOne(self, nums):
        #d = deque(nums)
        #d.append(d.popleft())# apparently deque doesn't support pop() method with any index it just removes elements from right, we ned to use popleft().

# we can do the sam ework using rotate() method of deque (it is not availabble in standard list), this method rotates the elements in a list a negative number rotates left, and a positive number rotates right and how much it gets rotated is written in the input of the method.
