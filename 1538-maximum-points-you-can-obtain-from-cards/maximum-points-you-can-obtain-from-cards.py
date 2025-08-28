class Solution(object):
    def maxScore(self, cardPoints, k):
        sum_k = max_sum = sum(cardPoints[:k])
        l, r = k - 1, len(cardPoints) - 1
        while l >= 0:
            sum_k -= cardPoints[l]
            sum_k += cardPoints[r]
            l -= 1
            r -= 1
            max_sum = max(max_sum, sum_k)
        return max_sum

        

       



        