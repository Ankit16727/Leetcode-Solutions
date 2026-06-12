class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Good Implementation problem. Logic is easy but edge cases noticing is easy but it's just
        # implementation part which seems more of a hard part.
        n1, n2 = "0", "0"
        i1, i2 = 0, 0

        while i1 <= len(version1) or i2 <= len(version2):
            m1 = i1 < len(version1) and version1[i1] != '.'
            m2 = i2 < len(version2) and version2[i2] != '.'

            if m1:
                if version1[i1] == 0:
                    if int(n1) > 0:
                        n1 += version1[i1]
                else:
                    n1 += version1[i1]
                i1 += 1
            
            if m2:
                if version2[i2] == 0:
                    if int(n2) > 0:
                        n2 += version2[i2]
                else:
                    n2 += version2[i2]
                i2 += 1
            
            if not m1 and not m2:
                if int(n1) > int(n2):
                    return 1
                elif int(n1) < int(n2):
                    return -1
                i1 += 1
                i2 += 1
                n1, n2 = "0", "0"
        
        return 0





        