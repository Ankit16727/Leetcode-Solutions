class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        ## [13:1, 12:2, 11:3]
        # implementation seems a bit hard
        # "aaaaaabbbbbbb"

        ## 14 : 1, 13 : 2, 12 : 3
        cnt = 1
        hMap = {}
        mx = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                if cnt > mx:
                    for i2 in range(mx + 1, cnt + 1):
                        k = s[i] + str(i2)
                        hMap[k] = hMap.get(k, 0) + (cnt - i2 + 1)
                        if hMap[k] >= 3:
                            mx = i2
            else:
                if s[i] != s[i + 1]:
                    if cnt > mx:
                        for i2 in range(mx + 1, cnt + 1):
                            k = s[i] + str(i2)
                            hMap[k] = hMap.get(k, 0) + (cnt - i2 + 1)
                            if hMap[k] >= 3:
                                mx = i2
                    
                    cnt = 1
                else:
                    cnt += 1
            
        
        return -1 if mx == 0 else mx


        