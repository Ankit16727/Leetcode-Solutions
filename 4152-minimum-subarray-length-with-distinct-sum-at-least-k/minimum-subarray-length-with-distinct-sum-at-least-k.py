class Solution(object):
    def minLength(self, nums, k):
        l, w_sum, min_len, nums_hash = 0, 0, None, {}
        for r in range(len(nums)):
            # Checking if it's unique in the window
            if nums[r] not in nums_hash or nums_hash[nums[r]] == 0:
                w_sum += nums[r]
            nums_hash[nums[r]] = nums_hash.get(nums[r], 0) + 1

            while w_sum >= k:
                min_len = r - l + 1 if min_len is None else min(min_len, r - l + 1)
                if min_len == 1:
                    return 1
                nums_hash[nums[l]] -= 1
                if nums_hash[nums[l]] == 0:
                    w_sum -= nums[l]
                l += 1
        return -1 if min_len is None else min_len
                

        