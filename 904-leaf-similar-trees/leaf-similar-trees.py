# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        tree1_leaf = self.leafSimilarRec(root1, ())
        tree2_leaf = self.leafSimilarRec(root2, ())
        return tree1_leaf == tree2_leaf
        
    def leafSimilarRec(self, root, leaf_nodes):
        if root is None:
            return leaf_nodes
        elif root.left is None and root.right is None:
            return leaf_nodes + (root.val,)
        leaf_nodes_l = self.leafSimilarRec(root.left, leaf_nodes)
        return self.leafSimilarRec(root.right, leaf_nodes_l)

        