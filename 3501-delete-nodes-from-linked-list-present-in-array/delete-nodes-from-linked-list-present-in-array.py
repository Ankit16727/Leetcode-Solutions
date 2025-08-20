# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        
        curr = head
        prev = None

        while curr != None:
            if curr.val in hm:
                if curr is head:
                    head = curr.next
                    curr.next = None
                    curr = head
                else:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return head

            

