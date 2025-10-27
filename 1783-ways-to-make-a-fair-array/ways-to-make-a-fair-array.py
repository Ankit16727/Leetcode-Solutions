class Solution(object):
    def waysToMakeFair(self, nums):
        e_sum, o_sum = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                e_sum += nums[i]
            else:
                o_sum += nums[i]
        
        pref_e, pref_o, cnt = 0, 0, 0
        for i in range(len(nums)):
            odd, even = 0, 0
            if i % 2 == 0:
                odd = pref_o + (e_sum - (pref_e + nums[i]))
                even = pref_e + (o_sum - pref_o)
                pref_e += nums[i]
            else:
                odd = pref_o + (e_sum - pref_e)
                even = pref_e + (o_sum - (pref_o + nums[i]))
                pref_o += nums[i]
            if even == odd:
                cnt += 1

        return cnt

        