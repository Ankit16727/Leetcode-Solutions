class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        min_idx, max_idx, l, total_sub, cnt = None, None, 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == minK:
                min_idx = r
            
            if nums[r] == maxK:
                max_idx = r
            
            if nums[r] < minK or nums[r] > maxK:
                # Invalid
                invalid_subs = cnt * (len(nums) - r)
                total_sub -= invalid_subs
                l, min_idx, max_idx, cnt = r + 1, None, None, 0
                
            
            if min_idx != None and max_idx != None:
                # We have found both the min and the max.
                total_sub += (min(min_idx, max_idx) - l + 1) * (len(nums) - r)
                cnt += min(min_idx, max_idx) - l + 1
                l = min(min_idx, max_idx) + 1
                if min_idx == max_idx:
                    min_idx, max_idx = None, None
                elif min_idx < max_idx:
                    min_idx = None
                else:
                    max_idx = None
        
        return total_sub

        