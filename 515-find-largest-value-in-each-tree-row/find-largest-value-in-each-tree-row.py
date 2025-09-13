# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        max_vals = []

        while len(queue) != 0:
            no_nodes = len(queue)
            max_v = None
            for i in range(no_nodes):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)
                
                max_v = node.val if max_v is None else max(max_v, node.val)

            max_vals.append(max_v)

        return max_vals 
        