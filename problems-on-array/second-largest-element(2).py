from collections import deque
class Solution:
    def secondLargestElement(self, nums):
        s = set(nums)
        if len(s) > 1:
            pass
        else:
            return -1
        row = deque(list(s))
        for w in range(len(row)-1):
                if row[0]< row[w+1]:
                    row[0],row[w+1] = row[w+1],row[0]
        first_item = row.popleft()
        for w in range(len(row)-1):
                if row[0]< row[w+1]:
                    row[0],row[w+1] = row[w+1],row[0]
        second_item = row.popleft()
        return second_item

