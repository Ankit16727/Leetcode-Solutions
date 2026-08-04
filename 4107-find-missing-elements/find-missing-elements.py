class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        missing = []
        l = nums[0] + 1

        i = 1

        while i < len(nums):
            if l == nums[i]:
                i += 1
            else:
                missing.append(l)
            l += 1
        
        return missing

        
        