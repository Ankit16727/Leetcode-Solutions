class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        l, r, cnt, cycle = 0, 1, 0, False
        while l != len(colors) and cycle == False:
            if colors[r] == colors[r - 1]:
                if r < l:
                    cycle = True
                l = r
            if l <= r:
                if r - l + 1 == k:
                    cnt += 1
                    l += 1
            else:
                if r + 1 + (len(colors) - l) == k:
                    cnt += 1
                    l += 1

            if r == len(colors) - 1:
                r = -1
            r += 1
        
        return cnt

        