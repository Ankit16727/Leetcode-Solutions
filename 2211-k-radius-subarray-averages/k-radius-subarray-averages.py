class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 6/2 -> 0 1 2 3 4 5 6 
        wS = 2 * k + 1
        ans = [-1] *  len(nums)
        l, sW = 0, 0
        for r in range(len(nums)):
            sW += nums[r]
            if r - l + 1 == wS:
                avg = sW // wS
                ans[(l + r) / 2] = avg
                sW -= nums[l]
                l += 1
        
        return ans


        