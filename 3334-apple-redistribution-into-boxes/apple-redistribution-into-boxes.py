class Solution(object):
    def minimumBoxes(self, apple, capacity):
        t_apples, nb = sum(apple), 0
        capacity.sort(reverse=True)

        for i in range(len(capacity)):
            nb += 1
            t_apples -= capacity[i]
            if t_apples <= 0:
                return nb



        