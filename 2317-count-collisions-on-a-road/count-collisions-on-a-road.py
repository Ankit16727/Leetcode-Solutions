class Solution(object):
    def countCollisions(self, directions):
        no_col, ri, f = 0, None, directions[0]
        for i in range(1, len(directions)):
            s = directions[i]
            # Conditions for collision happening
            if f == 'S' and s == 'L':
                no_col += 1
                f = 'S'
            elif f == 'R' and s == 'L':
                no_col += 2 if ri == None else i - ri + 1
                ri = None
                f = 'S'
            elif f == 'R' and s == 'S':
                no_col += 1 if ri == None else i - ri
                ri = None
                f = 'S'
            elif f == 'R' and s == 'R':
                ri = i - 1 if ri == None else ri
            else:
                # f = 'L'
                f = s
        return no_col