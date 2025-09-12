# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        # using a deque
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        level = 1

        while len(queue) != 0:
            no_nodes = len(queue)
            traversal = []
            for i in range(no_nodes):
                node = queue.pop() if level % 2 == 0 else queue.popleft()
                traversal.append(node.val)
                if level % 2 == 0:
                    if node.right != None:
                        queue.appendleft(node.right)
                    if node.left != None:
                        queue.appendleft(node.left)
                else:
                    if node.left != None:
                        queue.append(node.left)
                    
                    if node.right != None:
                        queue.append(node.right)
            level += 1
            
            result.append(traversal)

        return result
                
                

        