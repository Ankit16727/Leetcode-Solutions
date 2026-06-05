class Solution(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        p1 = 0
        no = 0
        for p2 in range(1, len(nums)):
            if nums[p2] > nums[p1]:
                p1 += 1
                no += 1
        
        return no
        
        