class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, i2, cnt = 0, 0, 0

        while i < len(g) and i2 < len(s):
            if g[i] <= s[i2]:
                i += 1
                i2 += 1
                cnt += 1
            else:
                i2 += 1
        return cnt

        