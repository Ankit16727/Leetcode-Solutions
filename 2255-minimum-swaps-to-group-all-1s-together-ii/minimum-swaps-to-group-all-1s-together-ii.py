class Solution(object):
    def minSwaps(self, nums):
        windowSize = nums.count(1)
        l, r, size, cnt1, minSwaps = 0, 0, 0, 0, None

        if windowSize == 0:
            return 0
        else:
            while l != len(nums):
                size += 1
                if nums[r] == 1:
                    cnt1 += 1
                if size == windowSize:
                    minSwaps = windowSize - cnt1 if minSwaps == None else min(minSwaps, windowSize - cnt1)
                    if minSwaps == 0:
                        return 0
                    if nums[l] == 1:
                        cnt1 -= 1
                    l += 1
                    size -= 1
                if r == len(nums) - 1:
                    r = -1
                r += 1
            
            return minSwaps

        