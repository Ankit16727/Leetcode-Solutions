# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        right_view = []

        while len(q) != 0:
            no_nodes = len(q)

            for i in range(no_nodes):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                
                if node.right != None:
                    q.append(node.right)
                
                if i == no_nodes - 1:
                    right_view.append(node.val)
        
        return right_view



