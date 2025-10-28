class Solution(object):
    def waysToSplitArray(self, nums):
        total = sum(nums)
        pref_sum, cnt = 0, 0
        for i in range(len(nums) - 1):
            pref_sum += nums[i]
            r_sum = total - pref_sum
            if pref_sum >= r_sum:
                cnt += 1
        return cnt