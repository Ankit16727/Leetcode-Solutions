class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        else:
            hash_t = {}
            for i in range(len(t)):
                if t[i] in hash_t:
                    hash_t[t[i]] += 1
                else:
                    hash_t[t[i]] = 1


            l, cnt, sub_str, min_str = 0, 0, "", ""
            for r in range(len(s)):
                if s[r] in hash_t:
                    hash_t[s[r]] -= 1
                    if hash_t[s[r]] >= 0:
                        cnt += 1
                sub_str = s[l:r + 1]
                if cnt == len(t):
                    min_str = sub_str
                    while True:
                        if s[l] in hash_t:
                            hash_t[s[l]] += 1
                            if hash_t[s[l]] > 0:
                                cnt -= 1
                                break
                        l += 1
                        min_str = s[l:r + 1]
                    l += 1
                elif len(min_str) > 0:
                    if s[l] in hash_t:
                            hash_t[s[l]] += 1
                            if hash_t[s[l]] > 0:
                                cnt -= 1
                    l += 1
            return min_str

                        


        