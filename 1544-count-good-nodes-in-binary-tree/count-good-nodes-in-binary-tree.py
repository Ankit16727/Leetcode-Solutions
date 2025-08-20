# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        return self.recGoodNodes(root)

    def recGoodNodes(self, node, mx = None, cnt = 0):
        if node is None:
            return cnt
        else:
            if mx is None:
                mx = node.val
                cnt += 1
            else:
                if node.val >= mx:
                    cnt += 1
                    mx = node.val
        
        ret_val = self.recGoodNodes(node.left, mx, cnt)
        return self.recGoodNodes(node.right, mx, ret_val)
        