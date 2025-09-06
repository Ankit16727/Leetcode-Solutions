class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Understand the question correctly
        stack_s, stack_t = [], []
        for i in range(len(s)):
            if s[i] == '#':
                if len(stack_s) != 0:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
        
        for i in range(len(t)):
            if t[i] == '#':
                if len(stack_t) != 0:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        
        print(stack_s, stack_t)
        
        return stack_s == stack_t
            
            
            
        