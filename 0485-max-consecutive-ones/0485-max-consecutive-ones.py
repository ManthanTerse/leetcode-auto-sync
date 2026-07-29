class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        op = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l = i + 1
            else:
                op = max(op ,i - l + 1 )
        return op