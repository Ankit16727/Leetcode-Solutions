# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        ret = self.recIsBalanced(root)
        return ret != -1
    def recIsBalanced(self, root):
        if root is None:
            return 0
        left_val = self.recIsBalanced(root.left)
        if left_val == -1:
            return -1
        right_val = self.recIsBalanced(root.right)
        if right_val == -1:
            return -1
        print(left_val, right_val)
        
        if abs(right_val - left_val) > 1:
            return -1
        
        
        
        return max(left_val, right_val) + 1
        
        