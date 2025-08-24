# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        ret_val = self.recLeaf(root, target)
        return None if ret_val == True else root
        
    def recLeaf(self, root, target):
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True if root.val == target else False
        else:
            # A simple node.
            l_ret_val = self.recLeaf(root.left, target)
            r_ret_val = self.recLeaf(root.right, target)
            if l_ret_val is True and r_ret_val is True:
                root.left, root.right = None, None
                if root.val == target:
                    return True
            elif l_ret_val is True:
                root.left = None
            elif r_ret_val is True:
                root.right = None
            
            return False


