class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l,r, c_sum, max_sum, sum_arr = 0, 0, 0, 0,0
        nums_dist = {}
        prefix_sum = []

        for r in range(len(nums)):
            sum_arr += nums[r]
            prefix_sum.append(sum_arr)
            if nums[r] in nums_dist:
                if nums_dist[nums[r]] < l:
                    nums_dist[nums[r]] = r
                    c_sum += nums[r]
                else:
                    max_sum = max(c_sum, max_sum)
                    l = pos = nums_dist[nums[r]] + 1
                    nums_dist[nums[r]] = r
                    c_sum = sum_arr - prefix_sum[pos - 1]
                
            else:
                nums_dist[nums[r]] = r
                c_sum += nums[r]

        return max(max_sum, c_sum)
        