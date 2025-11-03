class Solution(object):
    def minCost(self, colors, neededTime):
        max_time, total, k, min_time = neededTime[0], neededTime[0], colors[0], 0

        for i in range(1, len(colors)):
            if colors[i] == k:
                max_time = max(max_time, neededTime[i])
                total += neededTime[i]
                if i == len(colors) - 1:
                    min_time += total - max_time
            else:
                min_time += total - max_time
                k, max_time, total = colors[i], neededTime[i], neededTime[i]

        return min_time
        