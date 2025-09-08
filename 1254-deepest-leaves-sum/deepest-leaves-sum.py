# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        return self.recLeaveSum(root, 0, 0, 0)[1]
    
    def recLeaveSum(self, root, currDepth, maxDepth, currSum):
        if root is None:
            return (maxDepth, currSum)
        elif root.left is None and root.right is None:
            if currDepth == maxDepth:
                return (maxDepth, currSum + root.val)
            elif currDepth > maxDepth:
                return (currDepth, root.val)
            else:
                return (maxDepth, currSum)
        
        newMaxDepth, newCurrSum = self.recLeaveSum(root.left, currDepth + 1, maxDepth, currSum)
        return self.recLeaveSum(root.right, currDepth + 1, newMaxDepth, newCurrSum)
        