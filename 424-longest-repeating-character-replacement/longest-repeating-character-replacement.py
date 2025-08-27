class Solution(object):
    def characterReplacement(self, s, k):
        l, hash_set, max_freq, max_freq_cnt, max_len = 0, {}, 0, 0, 0
        for r in range(len(s)):
            # Adding elements to the hash map and computing the count
            if s[r] in hash_set:
                hash_set[s[r]] += 1
            else:
                hash_set[s[r]] = 1
            if hash_set[s[r]] > max_freq:
                max_freq = hash_set[s[r]]
                max_freq_cnt = 1
            elif hash_set[s[r]] == max_freq:
                max_freq_cnt += 1
            no_change = (r - l + 1) - max_freq
            # Invalid condition
            while no_change > k:
                max_len = max(max_len, r - l)
                if hash_set[s[l]] == max_freq:
                    max_freq_cnt -= 1
                    if max_freq_cnt == 0:
                        max_freq -= 1
                hash_set[s[l]] -= 1
                l += 1
                no_change = (r - l + 1) - max_freq
        return max(max_len, len(s) - l)

            
                