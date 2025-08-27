class Solution(object):
    def hasAllCodes(self, s, k):
        total_dist_sub = 2 ** k
        total_possible = len(s) - k + 1

        if total_possible >= total_dist_sub:
            sub_hash, curr, cnt = {}, "", 0
            for r in range(len(s)):
                curr += s[r]
                if len(curr) == k:
                    if curr not in sub_hash:
                        sub_hash[curr] = 1
                        cnt += 1
                    curr = curr[1:]
                if cnt == total_dist_sub:
                    return True
        return False

        