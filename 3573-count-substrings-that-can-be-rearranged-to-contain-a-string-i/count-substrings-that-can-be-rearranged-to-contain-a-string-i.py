class Solution(object):
    def validSubstringCount(self, word1, word2):
        hash_word2 = {}
        for i in range(len(word2)):
            hash_word2[word2[i]] = hash_word2.get(word2[i], 0) + 1

        hash_word1, l, ch_found, no_subs = {}, 0, set(), 0
        for r in range(len(word1)):
            hash_word1[word1[r]] = hash_word1.get(word1[r], 0) + 1
            if word1[r] in hash_word2 and hash_word1[word1[r]] >= hash_word2[word1[r]]:
                ch_found.add(word1[r])
            
            while len(ch_found) == len(hash_word2):
                no_subs += len(word1) - r
                hash_word1[word1[l]] -= 1
                if word1[l] in hash_word2 and hash_word1[word1[l]] < hash_word2[word1[l]]:
                    ch_found.remove(word1[l])
                l += 1
        return no_subs


        

        