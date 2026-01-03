class Solution(object):
    def getDescentPeriods(self, prices):
        l, ns = 0, 0

        for r in range(1, len(prices)):
            if prices[r] != prices[r - 1] - 1:
                ns += ((r - l) * (r - l + 1)) // 2
                l = r
        ns += ((len(prices) - l) * (len(prices) - l + 1)) // 2
        return ns
        