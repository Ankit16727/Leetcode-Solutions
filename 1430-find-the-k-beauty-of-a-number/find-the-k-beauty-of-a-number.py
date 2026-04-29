class Solution(object):
    def divisorSubstrings(self, num, k):
        num_s = str(num)
        curr, cnt = "", 0
        for r in range(len(num_s)):
            curr += num_s[r]
            if len(curr) == k:
                curr_i = int(curr)
                if curr_i != 0 and num % curr_i == 0:
                    cnt += 1
                curr = curr[1:]
        
        return cnt

        