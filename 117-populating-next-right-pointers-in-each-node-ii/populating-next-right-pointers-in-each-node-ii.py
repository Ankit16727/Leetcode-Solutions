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
        q = deque()
        if root:
            q.append(root)
        
        while len(q) > 0:
            no_nodes, prev = len(q), None
            for i in range(no_nodes):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                if prev != None:
                    prev.next = node
                prev = node
            prev.next = None
        
        return root
        