# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isEvenOddTree(self, root):
        q = deque([root])
        l = 0

        while len(q) != 0:
            no_nodes = len(q)
            prev = None
            if l % 2 == 0:
                # even level
                for i in range(no_nodes):
                    node = q.popleft()
                    if node.val % 2 != 0:
                        if prev is None or prev < node.val:
                            if node.left != None:
                                q.append(node.left)
                            if node.right != None:
                                q.append(node.right)
                            prev = node.val
                        else:
                            return False
                    else:
                        return False
            else:
                # odd level
                for i in range(no_nodes):
                    node = q.popleft()
                    if node.val % 2 == 0:
                        if prev is None or prev > node.val:
                            if node.left != None:
                                q.append(node.left)
                            if node.right != None:
                                q.append(node.right)
                            prev = node.val
                        else:
                            return False
                    else:
                        return False

            l += 1
        
        return True
        