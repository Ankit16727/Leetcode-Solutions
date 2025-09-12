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
                l_nodes = []
                l_vals = []
                # Getting the nodes in the level
                while len(queue) != 0:
                    l_nodes.append(queue.popleft())
                
                # Preparing the next level in the queue
                for i in range(len(l_nodes)):
                    if l_nodes[i].left != None:
                        queue.append(l_nodes[i].left)
                    
                    if l_nodes[i].right != None:
                        queue.append(l_nodes[i].right)
                    # Storing the values
                    l_vals.append(l_nodes[i].val)
                
                traversal.append(l_vals)
            
            return traversal
                


                



        