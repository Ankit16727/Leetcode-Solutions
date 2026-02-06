class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        l, max_len = 0, 0
        for r in range(len(nums)):
            while nums[l] * k < nums[r]:
                l += 1
            max_len = max(max_len, r - l + 1)

        return len(nums) - max_len

        