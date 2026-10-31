class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        total = n*(n+1)//2
        asum = sum(nums)

        return total - asum