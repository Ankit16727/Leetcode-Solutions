class Solution(object):
    def checkStrings(self, s1, s2):
        

        if len(s1) != len(s2):
            return False
        else:
            odd_s1, even_s1 = {}, {}
            odd_s2, even_s2 = {}, {}
            # Both of their lengths are equal
            for i in range(len(s1)):
                if i % 2 == 0:
                    even_s1[s1[i]] = even_s1.get(s1[i], 0) + 1
                    even_s2[s2[i]] = even_s2.get(s2[i], 0) + 1
                else:
                    odd_s1[s1[i]] = odd_s1.get(s1[i], 0) + 1
                    odd_s2[s2[i]] = odd_s2.get(s2[i], 0) + 1
            
            for key in even_s1:
                if even_s1[key] != even_s2.get(key, 0):
                    return False
            
            for key in odd_s1:
                if odd_s1[key] != odd_s2.get(key, 0):
                    return False
            
            return True
            
        