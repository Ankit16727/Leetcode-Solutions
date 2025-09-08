class Solution(object):
    def minSwaps(self, s):
        stack, ns = [], 0
        for i in range(len(s)):
            if s[i] == '[':
                stack.append('[')
            else:
                # It's closing one ']'
                if len(stack) == 0:
                    ns += 1
                else:
                    stack.pop()
        
        return ns // 2 if ns % 2 == 0 else ns // 2 + 1

        