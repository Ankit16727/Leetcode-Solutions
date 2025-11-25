class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        l, mx_len = 0, 0
        for r in range(len(nums)):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
            elif r > l:
                if nums[r] > threshold or (nums[r - 1] % 2 == 0 and nums[r] % 2 == 0) or (nums[r - 1] % 2 != 0 and nums[r] % 2 != 0):
                    if nums[r] % 2 == 0 and nums[r] <= threshold:
                        l = r
                    else:
                        l = r + 1
            mx_len = max(mx_len, r - l + 1)
        
        return mx_len



        