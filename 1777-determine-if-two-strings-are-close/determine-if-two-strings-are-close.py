class Solution(object):
    def closeStrings(self, word1, word2):
        # Their length has to be same
        # They should have same number of distinct characters, and the characters should be same too
        # Occcurences should also match (count match)
        if len(word1) == len(word2):
            w1_hash = {}
            cnt_w1 = 0
            w2_hash = {}
            cnt_w2 = 0
            for i in range(len(word1)):
                if word1[i] in w1_hash:
                    w1_hash[word1[i]] += 1
                else:
                    w1_hash[word1[i]] = 1
                    cnt_w1 += 1
            
            for i in range(len(word2)):
                if word2[i] in w2_hash:
                    w2_hash[word2[i]] += 1
                else:
                    w2_hash[word2[i]] = 1
                    cnt_w2 += 1
            
            if cnt_w1 == cnt_w2:
                for key in w1_hash:
                    if key not in w2_hash:
                        return False
            else:
                return False

            
            w1_freq = {}
            cnt1 = 0
            w2_freq = {}
            cnt2 = 0
            for key in w1_hash.values():
                if key in w1_freq:
                    w1_freq[key] += 1
                else:
                    w1_freq[key] = 1
                    cnt1 += 1
            
            for key in w2_hash.values():
                if key in w2_freq:
                    w2_freq[key] += 1
                else:
                    w2_freq[key] = 1
                    cnt2 += 1
            
            if cnt1 == cnt2:
                for key in w1_freq:
                    if key in w2_freq:
                        if w1_freq[key] != w2_freq[key]:
                            return False
                    else:
                        return False
            else:
                return False
            
            return True
        
        return False
        
        