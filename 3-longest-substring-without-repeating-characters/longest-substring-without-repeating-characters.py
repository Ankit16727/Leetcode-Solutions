class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash_set, l, curr_max = {}, 0, 0

        for r in range(len(s)):
            if s[r] in hash_set and hash_set[s[r]] > 0:
                curr_max = max(r - l , curr_max)
                while s[l] != s[r]:
                    hash_set[s[l]] = 0
                    l += 1
                l += 1
            else:
                hash_set[s[r]] = 1
            
        return max(curr_max, len(s) - l)
        