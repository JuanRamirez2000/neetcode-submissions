# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        prev, curr = None, head
        
        prev = None
        curr = head

        while curr: #while curr doesnt point to null
            temp = curr.next # create temp node
            curr.next = prev # assign current node to previous
            prev = curr      # now we have reversed it so we need to get the one before
            curr = temp      # move one step to the right and start all over

        return prev # returns the new head