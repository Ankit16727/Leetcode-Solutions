class Solution(object):
    def checkInclusion(self, s1, s2):
        hash_s1 = {}
        for i in range(len(s1)):
            if s1[i] in hash_s1:
                hash_s1[s1[i]] += 1
            else:
                hash_s1[s1[i]] = 1
        
        l, cnt = 0, 0

        for r in range(len(s2)):
            if s2[r] in hash_s1:
                hash_s1[s2[r]] -= 1
                if hash_s1[s2[r]] < 0:
                    while s2[l] != s2[r]:
                        hash_s1[s2[l]] += 1
                        l += 1
                    hash_s1[s2[l]] += 1
                    l += 1
                    cnt = r - l + 1
                else:
                    cnt += 1

            else: 
                while l < r:
                    hash_s1[s2[l]] += 1
                    l += 1
                l += 1
                cnt = 0
            if cnt == len(s1):
                return True
        
        return False
        