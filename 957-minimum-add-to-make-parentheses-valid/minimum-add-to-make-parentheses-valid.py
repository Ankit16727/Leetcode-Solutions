class Solution(object):
    def minAddToMakeValid(self, s):
        n_open = 0
        n_close = 0
        for i in range(len(s)):
            if s[i] == '(':
                n_open += 1
            else:
                # ')'
                if n_open >= 1:
                    n_open -= 1
                else:
                    n_close += 1
        
        return n_open + n_close

        