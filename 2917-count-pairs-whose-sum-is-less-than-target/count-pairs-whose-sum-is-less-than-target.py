class Solution(object):
    def countPairs(self, nums, target):
        cnt = 0
        for i in range(len(nums)):
            for i2 in range(i + 1, len(nums)):
                if nums[i] + nums[i2] < target:
                    cnt += 1
        
        return cnt

        