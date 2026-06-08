class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """"""
        bcfd3[bc2[cd]3[gf]aa]
        [3, 2]          
        [bc, cd]   
        [3,3]
        [bccdcd, gf]     
        [3]
        [bccdcdgfgfgfaa] 
        bcfd + isDigit
        [n1]
        """
        nums_s = []
        str_s = []
        r_s = ""
        n = ""
        for i in range(len(s)):
            if s[i].isdigit():
                n += s[i]
            elif s[i] == '[':
                nums_s.append(int(n))
                str_s.append("") #initally, empty string
                n = ""
            elif s[i] == ']':
                d = nums_s.pop()
                c = str_s.pop()
                r = d * c
                if len(nums_s) != 0:
                    # element still there in the stack
                    str_s[-1] += r
                else:
                    r_s += r
            else:
                if len(str_s) != 0:
                    # the 
                    str_s[-1] += s[i]
                else:
                    # if it's 0
                    r_s += s[i]
            print(nums_s, str_s)
        return r_s

                

        