class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for i in range(len(asteroids)):
            add = True
            if asteroids[i] < 0:
                while len(stack) > 0 and stack[-1] > 0:
                    if abs(asteroids[i]) > stack[-1]:
                        stack.pop()
                    elif abs(asteroids[i]) < stack[-1]:
                        break
                    else:
                        # both equal
                        stack.pop()
                        add = False
                        break
                
                if len(stack) == 0:
                    if add:
                        stack.append(asteroids[i])
                elif stack[-1] < 0 and add :
                    stack.append(asteroids[i])
            else:
                # > 0
                stack.append(asteroids[i])
        
        return stack
        