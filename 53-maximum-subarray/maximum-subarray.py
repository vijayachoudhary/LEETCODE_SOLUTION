class Solution(object):
    def maxSubArray(self, nums):
        summ = nums[0]
        max_summ = nums[0]
        
        for i in range(1,len(nums)):

            summ = max(nums[i],summ +nums[i])

            max_summ = max(max_summ,summ)

        return max_summ    