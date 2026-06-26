class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # [a1, a2, a3, a4, a5, a6, a7]
        prefix_sums = []
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == target:
                cnt += 1
            
            prefix_sums.append(cnt)
        cnt_sub = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                t_sub = prefix_sums[j] - prefix_sums[i - 1] if i != 0 else prefix_sums[j]
                if t_sub > (j - i + 1) // 2:
                    cnt_sub += 1
        
        return cnt_sub

