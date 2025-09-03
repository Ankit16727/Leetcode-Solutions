# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        return self.recInorderTraversal(root, [])
    def recInorderTraversal(self, root, traverseList = []):
        if root is None:
            return traverseList
        l_list = self.recInorderTraversal(root.left, traverseList)
        l_list.append(root.val)
        return self.recInorderTraversal(root.right, l_list)
        
        