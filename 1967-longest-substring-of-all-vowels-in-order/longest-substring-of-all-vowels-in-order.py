class Solution(object):
    def longestBeautifulSubstring(self, word):
        vowels_hash = {'a': None,'e': 'a', 'i': 'e', 'o' : 'i', 'u' : 'o'}
        max_len = 0
        l = 0
        for r in range(len(word)):
            if l == r:
                if word[l] != 'a':
                    l += 1
            else:
                if word[r] == word[r - 1] or word[r - 1] == vowels_hash[word[r]]:
                    if word[r] == 'u':
                        max_len = max(max_len, r - l + 1)
                else:
                    l = r if word[r] == 'a' else r + 1

        return max_len

                

        