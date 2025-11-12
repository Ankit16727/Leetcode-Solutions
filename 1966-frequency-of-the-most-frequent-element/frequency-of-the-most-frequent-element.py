class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort(reverse = True)
        l, max_freq, curr, cnt = 0, 1, 0, 1
        for r in range(1, len(nums)):
            curr += nums[l] - nums[r]
            while curr > k:
                pref = nums[l] - nums[l + 1]
                l += 1
                curr -= (r - l + 1) * pref
            max_freq = max(max_freq, r - l + 1)
        return max_freq
            

        