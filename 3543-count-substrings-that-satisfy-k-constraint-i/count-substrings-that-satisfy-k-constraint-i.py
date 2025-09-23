class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        l, n1, n0, totalSubs = 0, 0, 0, 0

        for r in range(len(s)):
            if s[r] == '0':
                n0 += 1
            else:
                n1 += 1
            
            while min(n0, n1) > k:
                totalSubs += r - l
                if s[l] == '0':
                    n0 -= 1
                else:
                    n1 -= 1
                l += 1
        
        return totalSubs + ((len(s) - l) * (len(s) - l + 1)) // 2