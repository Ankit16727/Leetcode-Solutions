class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        sum0 = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sum0 += customers[i]
        
        l, cnt = 0, 0
        pref_0, cust, max_cust  = 0, 0, 0
        for i in range(len(customers)):
            cnt += 1
            if grumpy[i] == 0:
                pref_0 += customers[i]
            cust += customers[i]
            if cnt == minutes:
                max_cust = max(cust + sum0 - pref_0, max_cust)
                if grumpy[l] == 0:
                    pref_0 -= customers[l]
                cust -= customers[l]
                l += 1
                cnt -= 1
        return max_cust
            

        