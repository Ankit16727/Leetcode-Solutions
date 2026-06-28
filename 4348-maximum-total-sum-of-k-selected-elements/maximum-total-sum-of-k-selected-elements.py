class Solution(object):
    def maxSum(self, nums, k, mul):
        nums.sort(reverse=True)
        totalSum = 0

        for i in range(k):
            if mul > 0:
                totalSum += mul * nums[i]
                mul -= 1
            else:
                totalSum += nums[i]
        
        return totalSum


            

            

        