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
            for i in range(no_nodes):
                node = q.popleft()
                if l % 2 == 0:
                    if node.val % 2 == 0 or (prev is not None and prev >= node.val):
                        return False
                else:
                    if node.val % 2 != 0 or (prev is not None and prev <= node.val):
                        return False
                
                if node.left != None:
                     q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                prev = node.val

            l += 1
        
        return True
        