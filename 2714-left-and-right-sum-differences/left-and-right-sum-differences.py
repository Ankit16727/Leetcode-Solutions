class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        l_sum = 0
        ans = []
        for i in range(len(nums)):
            r_sum = total - (l_sum + nums[i])
            ans.append(abs(r_sum - l_sum))
            l_sum += nums[i]
        
        return ans
        