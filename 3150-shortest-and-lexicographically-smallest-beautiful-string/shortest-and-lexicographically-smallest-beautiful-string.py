class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        minStr, curStr, n1 = "", "", 0

        for r in range(len(s)):
            if s[r] == '1':
                n1 += 1
            curStr += s[r]
            while n1 == k:
                if len(minStr) == 0 or len(curStr) < len(minStr) or ((len(curStr) == len(minStr)) and curStr < minStr):
                    minStr = curStr
                if curStr[0] == '1':
                    n1 -= 1
                curStr = curStr[1:]
            
        return minStr

        
        