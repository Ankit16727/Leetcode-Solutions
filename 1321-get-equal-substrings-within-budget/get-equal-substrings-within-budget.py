class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        l, maxLen, currSum = 0, 0, 0
        for r in range(len(s)):
            currSum += abs(ord(s[r]) - ord(t[r]))
            
            while currSum > maxCost:
                currSum -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
        