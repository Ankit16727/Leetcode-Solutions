class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        f, s, t = len(nums) - 1 , len(nums) - 2 , len(nums) - 3

        while t >= 0:
            if nums[s] + nums[t] > nums[f]:
                return nums[f] + nums[s] + nums[t]
            f -= 1
            s -= 1
            t -= 1
        
        return 0

        