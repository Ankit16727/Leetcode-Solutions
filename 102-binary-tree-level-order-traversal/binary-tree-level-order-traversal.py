# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        else:
            traversal = []
            queue = deque()
            queue.append(root)
            while len(queue) != 0:
                l_vals = []
                no_nodes = len(queue)
                for i in range(no_nodes):
                    node = queue.popleft()
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)
                    l_vals.append(node.val)
                traversal.append(l_vals)
            
            return traversal
                


                



        