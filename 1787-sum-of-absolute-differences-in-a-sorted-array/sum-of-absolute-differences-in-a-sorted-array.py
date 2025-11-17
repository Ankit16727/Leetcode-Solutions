class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        total = 0
        for i in range(1, len(nums)):
            total += nums[i] - nums[0]
        pref_sum, ans = 0, []
        for i in range(len(nums)):
            pref_sum += nums[i] - nums[0]
            if i == 0:
                ans.append(total)
            else:
                k = nums[i] - nums[0]
                sum_dist = ((total - pref_sum) - ((len(nums) - i - 1) * k)) + ((i + 1) * k - pref_sum)
                ans.append(sum_dist)
            
        return ans


        