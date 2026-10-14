class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The problem basically translates to:
        nums.sort()
        l = 0
        r = len(nums) - 1
        noPos = len(nums) // 2 if len(nums) % 2 == 0 else (len(nums) + 1) // 2
        oddSum = 0
        evenSum = 0

        while l <= r:
            if noPos > 0:
                if nums[l] ** 2 >= nums[r] ** 2:
                    oddSum += nums[l] ** 2
                    l += 1
                else:
                    oddSum += nums[r] ** 2
                    r -= 1
                noPos -= 1
            else:
                evenSum += nums[l] ** 2
                l += 1
        
        return oddSum - evenSum




        

        
         
        