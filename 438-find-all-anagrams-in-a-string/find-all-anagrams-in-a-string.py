class Solution(object):
    def findAnagrams(self, s, p):
        # Creating a hash map of string 'p', storing the count of each character
        hash_p = {}
        for i in range(len(p)):
            if p[i] in hash_p:
                hash_p[p[i]] += 1
            else:
                hash_p[p[i]] = 1
        
        hash_s, l, r, count, indices = {}, 0, 0, 0, []

        while l <= len(s) - len(p):
            if s[r] in hash_p:
                if s[r] in hash_s:
                    hash_s[s[r]] += 1
                    count += 1
                    if hash_s[s[r]] > hash_p[s[r]]:
                        while s[l] != s[r]:
                            hash_s[s[l]] -= 1
                            l += 1
                            count -= 1
                        hash_s[s[l]] -= 1
                        l += 1
                        count -= 1
                else:
                    hash_s[s[r]] = 1
                    count += 1
                
                if count == len(p):
                    indices.append(l)
                    hash_s[s[l]] -= 1
                    count -= 1
                    l += 1
            else:
                hash_s, count, l = {}, 0, r + 1
            r += 1
        
        return indices