class Solution(object):
    def maxSum(self, nums, m, k):
        mx_sum, l, w_sum, n_unq, nums_hash = 0, 0, 0, 0, {}
        for r in range(len(nums)):
            if nums[r] not in nums_hash:
                nums_hash[nums[r]] = 1
                n_unq += 1
            else:
                if nums_hash[nums[r]] == 0:
                    n_unq += 1
                nums_hash[nums[r]] += 1
            # Calculating the sum
            w_sum += nums[r]
            if r - l + 1 == k:
                if n_unq >= m:
                    mx_sum = max(mx_sum, w_sum)
                w_sum -= nums[l]
                nums_hash[nums[l]] -= 1
                if nums_hash[nums[l]] == 0:
                    n_unq -= 1
                l += 1
        return mx_sum

        