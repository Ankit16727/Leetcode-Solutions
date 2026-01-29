class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        l, min_diff = 0,  None

        for r in range(k - 1, len(nums)):
            min_diff = nums[r] - nums[l] if min_diff is None else min(min_diff, nums[r] - nums[l])
            l += 1
        
        return min_diff
        