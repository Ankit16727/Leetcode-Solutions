# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        averages = []
        while len(queue) != 0:
            # There are still nodes in the level
            no_nodes = len(queue)
            sum_nodes = 0.0
            for i in range(no_nodes):
                node = queue.popleft()
                sum_nodes += node.val
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            averages.append(sum_nodes / no_nodes)
        
        return averages
            
                
                


        
        