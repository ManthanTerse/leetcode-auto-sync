class Solution(object):
    def shuffle(self, nums, n):
        n = len(nums)/2
        ans = []
        for i in range(n):
             ans.append(nums[i])
             ans.append(nums[n+i])      
        return ans