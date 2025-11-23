class Solution(object):
    def bestClosingTime(self, customers):
        ty = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                ty += 1
        
        nn, py, min_p, h = 0, 0, None, None
        for i in range(len(customers) + 1):
            ny = ty - py
            if i == 0:
                min_p = ny
                h = 0
            elif ny + nn < min_p:
                min_p = nn + ny
                h = i
            if i < len(customers):
                if customers[i] == 'N':
                    nn += 1
                else:
                    py += 1
        
        return h

        