class Solution(object):
    def minSizeSubarray(self, nums, target):
        sum_nums = sum(nums)
        n_target = target % sum_nums
        initial_length = (target // sum_nums) * len(nums)
        if n_target == 0:
            return initial_length
        else:
            l, r, w_sum, min_len = 0, 0, 0, None
            while l < len(nums):
                r = r % len(nums)
                w_sum += nums[r]
                while w_sum > n_target and l < len(nums):
                    w_sum -= nums[l]
                    l += 1
                
                if w_sum == n_target and l < len(nums):
                    w_len = None
                    if l <= r:
                        w_len = r - l + 1
                    else:
                        w_len = (len(nums) - l) + (r + 1)
                    min_len = w_len if min_len is None else min(w_len, min_len)
                    w_sum -= nums[l]
                    l += 1
                r += 1
            return -1 if min_len is None else initial_length + min_len
        