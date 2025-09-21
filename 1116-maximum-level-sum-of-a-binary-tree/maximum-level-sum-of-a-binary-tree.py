# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        q = deque()
        q.append(root)
        level = 1
        min_level = None
        max_sum = None
        while len(q) != 0:
            no_nodes = len(q)
            level_sum = 0
            for i in range(no_nodes):
                node = q.popleft()
                if node.right != None:
                    q.append(node.right)
                
                if node.left != None:
                    q.append(node.left)
                level_sum += node.val
            if max_sum is None:
                max_sum = level_sum
                min_level = level
            else:
                if level_sum > max_sum:
                    max_sum = level_sum
                    min_level = level
            level += 1
        
        return min_level

            

