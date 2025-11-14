class Solution(object):
    def findPrefixScore(self, nums):
        ans, pref_score, max_score = [], 0, 0
        for i in range(len(nums)):
            max_score = max(nums[i] , max_score)
            score_i = pref_score + (nums[i] + max_score)
            ans.append(score_i)
            pref_score = score_i

        return ans 
        