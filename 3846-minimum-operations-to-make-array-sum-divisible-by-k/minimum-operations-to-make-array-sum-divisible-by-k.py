class Solution(object):
    def minOperations(self, nums, k):
        sum_arr = sum(nums)
        return sum_arr % k
        