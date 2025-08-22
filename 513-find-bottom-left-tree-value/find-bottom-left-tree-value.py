# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        return self.recBottomLeftValue(root)[1]

    def recBottomLeftValue(self, node, cd = 0, md = None, lval = None):
        if node is None:
            return (md, lval)
        elif node.left is None and node.right is None:
            # It's a leaf node
            if cd + 1 > md:
                return (cd + 1, node.val)
            else:
                return (md, lval)
        else:
            ret = self.recBottomLeftValue(node.left, cd + 1, md, lval)
            return self.recBottomLeftValue(node.right, cd +1, ret[0], ret[1])

        