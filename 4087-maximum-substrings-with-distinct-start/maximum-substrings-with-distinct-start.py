class Solution(object):
    def maxDistinct(self, s):
        distChars = set()
        for i in range(len(s)):
            distChars.add(s[i])
        
        return len(distChars)
        