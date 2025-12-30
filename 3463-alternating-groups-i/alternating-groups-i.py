class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        l, r, n_al = 0, 1, 0
        while l < len(colors):
            r = r % len(colors)
            if colors[r] == colors[r - 1]:
                if r >= l:
                    l = r
                else:
                    l = len(colors)
            if r == (l + 2) % len(colors):
                n_al += 1
                l += 1
            
            r += 1
        return n_al

        