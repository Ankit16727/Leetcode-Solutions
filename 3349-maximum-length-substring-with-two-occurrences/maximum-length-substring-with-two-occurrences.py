class Solution(object):
    def maximumLengthSubstring(self, s):
        l, max_len, mx_freq, s_hash = 0, 0, 0, {}
        for r in range(len(s)):
            if s[r] in s_hash:
                s_hash[s[r]] += 1
            else:
                s_hash[s[r]] = 1
            mx_freq = max(mx_freq, s_hash[s[r]])

            while mx_freq > 2:
                if s_hash[s[l]] == 3:
                    mx_freq -= 1
                s_hash[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len

        