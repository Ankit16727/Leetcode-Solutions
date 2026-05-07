class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        l, r, u = 0, 0, 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                l += 1
            elif moves[i] == 'R':
                r += 1
            else:
                u += 1
        
        return abs(r - l) + u
        