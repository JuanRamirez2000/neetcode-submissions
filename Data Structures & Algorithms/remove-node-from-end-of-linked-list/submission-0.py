# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0 
        curr = head
        while curr:
            size += 1 
            curr = curr.next
        
        i = 0
        dumm = ListNode()
        dumm.next = head

        curr = dumm
        while i < size and curr.next:
            if i == (size - n):
                i += 1
                curr.next = curr.next.next
            else:
                i += 1
                curr = curr.next
        return dumm.next
