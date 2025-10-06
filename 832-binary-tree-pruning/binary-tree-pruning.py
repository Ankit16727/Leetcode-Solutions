# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        ret = self.recTree(root)
        return None if ret == False else root
    
    def recTree(self, root):
        if root is None:
            return False
        else:
            left = self.pruneTree(root.left)
            if not left:
                root.left = None
            right = self.pruneTree(root.right)
            if not right:
                root.right = None
            if left or right or root.val == 1:
                return True
            else:
                return False