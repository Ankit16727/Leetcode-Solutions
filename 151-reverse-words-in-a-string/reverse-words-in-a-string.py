class Solution(object):
    def reverseWords(self, s):
        i = len(s) - 1
        final_string = ""
        curr_word = ""
        while i >= 0:
            if s[i] == " " and len(curr_word) > 0:
                if len(final_string) > 0:
                    final_string = final_string + " " + curr_word
                else:
                    final_string = final_string + curr_word

                curr_word = ""
            if s[i] != " ":
                curr_word = s[i] + curr_word
            
            if i == 0 and len(curr_word) > 0:
                if len(final_string) > 0:
                    final_string = final_string + " " + curr_word
                else:
                    final_string = final_string + curr_word
            i -= 1
        
        return final_string
        