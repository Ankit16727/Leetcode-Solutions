class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [2,1,1,1,2,2,2,3,1,2,3,3,5,2,2,1,1,3]

        # count in the window, finding the boundary till where it can go.
        # ends when window last index goes out of range
        # while count_dist == k and window_li < boundary
        l, boundary = 0, None
        w, cnt_dist = {}, 0
        ts = 0

        for r in range(len(nums)):
            # calculating the window
            w[nums[r]] = w.get(nums[r], 0) + 1
            if w[nums[r]] == 1:
                cnt_dist += 1
            
            # calculating the boundary
            if cnt_dist == k and (boundary == None or r == boundary):
                if r == len(nums) - 1:
                    boundary = len(nums)
                else:
                    for i in range(r + 1, len(nums)):
                        if nums[i] not in w or w[nums[i]] == 0:
                            boundary = i
                            break
                        elif i == len(nums) - 1:
                            boundary = len(nums)
            
            while cnt_dist == k:
                ts += boundary - r
                w[nums[l]] -= 1
                if w[nums[l]] == 0:
                    cnt_dist -= 1
                l += 1
        
        return ts


            


        
        