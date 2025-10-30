class Solution(object):
    def maxScore(self, s):
        total_ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                total_ones += 1
        
        z, o, max_sum = 0, 0, 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                z += 1
            else:
                o += 1
            max_sum = max(max_sum, z + (total_ones - o))
        
        return max_sum
        