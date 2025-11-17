class Solution(object):
    def minOperations(self, boxes):
        total, n_1 = 0, 0

        for i in range(len(boxes)):
            if boxes[i] == '1':
                n_1 += 1
                total += i
        
        pref_cnt1, pref, ans = 0, 0, []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                pref_cnt1 += 1
                pref += i
            
            if i == 0:
                ans.append(total)
            else:
                min_opr = (i * pref_cnt1 - pref) + ((total - pref) - ((n_1 - pref_cnt1)* i))
                ans.append(min_opr)
        
        return ans

        