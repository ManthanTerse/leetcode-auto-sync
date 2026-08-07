class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans = []
        n = len(nums)
        s = set(nums)
        for i in range(1, n+1):
            if i not in s:
                ans.append(i)
        return ans