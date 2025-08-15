class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_count = -1
        count = 0
        t_sum = 0
        c_sum = 0
        p_sum = 0
        l = 0
        h = 0

        while l <= h and h < len(nums):
            if min_count == -1:
                c_sum += nums[h]
                t_sum += nums[h]
                count += 1
                if c_sum >= target:
                    min_count = count
                    count = 0
                    p_sum += nums[l]
                    l = l + 1
                else:
                    h = h + 1
            else:
                c_sum = t_sum - p_sum
                if c_sum >= target:
                    count = h - l + 1
                    min_count = count
                    p_sum += nums[l]
                    l = l + 1
                else:
                    p_sum += nums[l]
                    l = l + 1
                    h = h + 1
                    if h < len(nums):
                        t_sum += nums[h]
            

        if min_count == -1:
            return 0 
        else:
            return min_count

            




        
        