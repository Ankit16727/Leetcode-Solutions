class Solution(object):
    def countPartitions(self, nums):
        total = sum(nums)
        left_sum, no = 0, 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum

            if (left_sum - right_sum) % 2 == 0:
                no += 1
        
        return no


        