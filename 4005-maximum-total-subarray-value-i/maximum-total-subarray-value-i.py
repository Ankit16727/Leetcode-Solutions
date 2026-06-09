class Solution(object):
    def maxTotalValue(self, nums, k):
        mx, mn = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > mx:
                mx = nums[i]
            
            if nums[i] < mn:
                mn = nums[i]
            
        
        return (mx - mn) * k
        