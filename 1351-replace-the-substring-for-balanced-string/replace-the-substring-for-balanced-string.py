class Solution(object):
    def balancedString(self, s):
        nq, nw, ne, nr = 0, 0, 0, 0
        for i in range(len(s)):
            nq += (s[i] == 'Q')
            nw += (s[i] == 'W')
            ne += (s[i] == 'E')
            nr += (s[i] == 'R')
        req = len(s) // 4
        if nq == nw == ne == nr:
            return 0
        nq -= req
        nw -= req
        ne -= req
        nr -= req

        l, min_len, ch_hash = 0, None, {}
        for r in range(len(s)):
            ch_hash[s[r]] = ch_hash.get(s[r], 0) + 1

            while ch_hash.get('Q', 0) >= nq and ch_hash.get('W', 0) >= nw and ch_hash.get('E', 0) >= ne and ch_hash.get('R', 0) >= nr:
                min_len = r - l + 1 if min_len is None else min(min_len, r - l + 1)
                ch_hash[s[l]] -= 1
                l += 1
        
        return min_len
        