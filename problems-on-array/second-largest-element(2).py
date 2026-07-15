class Solution:
    def secondLargestElement(self, nums):
        first = float("-inf")
        second = float("-inf")

        for num in nums:
            if num > second and num > first:
                first, second = num, first
            elif num > second and num < first:
                second = num
            elif num > second and num == first:
                pass

        if first != second and second != float("-inf"):
            return second
        elif second == float("-inf"):
            return -1
        else:
            return -1
