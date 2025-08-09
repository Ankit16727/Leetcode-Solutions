class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        c = 0
        for i in range(len(nums1)):
            for i2 in range(len(nums2)):
                if nums1[i] % (nums2[i2] * k) == 0:
                    c += 1
        
        return c
        