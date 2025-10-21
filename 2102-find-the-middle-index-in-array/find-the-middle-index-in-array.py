class Solution(object):
    def findMiddleIndex(self, nums):
        total_sum = sum(nums)
        pref_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            r_sum = total_sum - pref_sum
            l_sum = pref_sum - nums[i]
            if r_sum == l_sum:
                return i
        
        return -1
            
            