"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            no_nodes = len(queue)
            f,s  = queue.popleft(), None
            for i in range(no_nodes):
                if f.left != None:
                    queue.append(f.left)
                if f.right != None:
                    queue.append(f.right)
                if i != no_nodes - 1:
                    s = queue.popleft()
                    f.next = s
                    f = s
                
            f.next = None

        return root
                
                
                


        
        