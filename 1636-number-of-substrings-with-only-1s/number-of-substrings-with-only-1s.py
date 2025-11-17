class Solution(object):
    def numSub(self, s):
        cnt_1, total = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt_1 += 1
            else:
                # it's 0
                total += (cnt_1 * (cnt_1 + 1)) // 2
                cnt_1 = 0
        total += (cnt_1 * (cnt_1 + 1)) // 2
        return total % (10**9 + 7)
        


        