class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j, cnt, s = 0, 0, 1, ""
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                if cnt % 2 == 0:
                    s = s + word2[j]
                    j += 1
                else:
                    s = s + word1[i]
                    i += 1
                cnt += 1
            elif i < len(word1):
                while i < len(word1):
                    s += word1[i]
                    i += 1
            else:
                # j < len(word2)
                while j < len(word2):
                    s += word2[j]
                    j += 1
        return s