class Solution(object):
    def distinctPoints(self, s, k):
        nU = s.count('U')
        nD = s.count('D')
        nL = s.count('L')
        nR = s.count('R')
        l = 0
        counts = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        sDist = set()
        for r in range(len(s)):
            counts[s[r]] += 1
            if r - l + 1 == k:
                point = (((nU - counts['U']) - (nD - counts['D'])), ((nR - counts['R']) - (nL - counts['L'])))
                if point not in sDist:
                    sDist.add(point)
                counts[s[l]] -= 1
                l += 1
        
        return len(sDist)


        