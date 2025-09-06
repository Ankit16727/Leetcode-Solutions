class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Understand the question correctly
        # O(n) -> space complexity.
        """
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
        """
        # 2 pointer approach
        # O(1) -> extra space complexity
        si, ti, ns, nt = len(s) - 1, len(t) - 1, 0, 0
        while si >= 0 or ti >= 0:
            if si >= 0 and ti >= 0:
                if s[si] != '#' and t[ti] != '#' and ns == 0 and nt == 0:
                    if s[si] != t[ti]:
                        return False
                    si -= 1
                    ti -= 1
                
            if si >= 0:
                if s[si] == '#':
                    ns += 1
                    si -= 1
                else:
                    if ns > 0:
                        ns -= 1
                        si -= 1
                    elif ti < 0:
                        return False
                
            if ti >= 0:
                if t[ti] == '#':
                    nt += 1
                    ti -= 1
                else:
                    if nt > 0:
                        nt -= 1
                        ti -= 1
                    elif si < 0:
                        return False
        return True
        
        
            
            
            
            
            
            
            
        