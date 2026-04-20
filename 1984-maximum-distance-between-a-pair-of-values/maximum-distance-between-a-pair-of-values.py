class Solution(object):
    def maxDistance(self, nums1, nums2):
        l, r = 0, 0
        maxD = 0
        while l <len(nums1) and r < len(nums2):
            while l < len(nums1) and l <= r and nums1[l] > nums2[r]:
                l += 1

            maxD = max(maxD, r - l)
            r += 1
        return maxD