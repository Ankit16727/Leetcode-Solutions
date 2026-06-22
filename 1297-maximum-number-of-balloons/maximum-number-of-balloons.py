class Solution(object):
    def maxNumberOfBalloons(self, text):
        cHash = {}
        for i in range(len(text)):
            cHash[text[i]] = cHash.get(text[i], 0) + 1
        
        print(cHash)
        
        mn = None
        for ch in ['b', 'a', 'l', 'o', 'n']:
            cnt = cHash.get(ch, 0) 
            if ch == 'l' or ch == 'o':
                cnt = cnt // 2
            
            mn = cnt if mn is None else min(mn, cnt)

        return mn
            




