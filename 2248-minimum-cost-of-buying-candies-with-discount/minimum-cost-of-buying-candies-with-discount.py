class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        [9,7,6,5,2,2]
        """
        ts = sum(cost)
        cost.sort(reverse=True)
        i = 2
        while i < len(cost):
            ts -= cost[i]
            i += 3
        
        return ts
