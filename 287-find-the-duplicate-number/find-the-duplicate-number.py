class Solution(object):
    def findDuplicate(self, nums):
        # 1st way can be to sort the list. Numbers can only be in the range [1, n]
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        
        