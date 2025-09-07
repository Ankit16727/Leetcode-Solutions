class Solution(object):
    def simplifyPath(self, path):
        stack, dr = [], ""
        for i in range(len(path)):
            if path[i] == '/':
                if len(dr) > 0 and dr != ".":
                    if dr == "..":
                        if len(stack) != 0:
                            stack.pop()
                    else:
                        stack.append(dr)
                dr = "" 
            else:
                dr += path[i]
                print(dr)
                if i == len(path) - 1:
                    if dr != ".":
                        if dr == "..":
                            if len(stack) != 0:
                                stack.pop()
                        else:
                            stack.append(dr)
        
        return "/" + "/".join(stack)

            
