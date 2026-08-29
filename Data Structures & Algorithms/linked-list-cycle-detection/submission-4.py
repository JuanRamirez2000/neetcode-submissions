# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head

        if ptr1.next is None:
            return False

        ptr2 = head.next.next

        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return True
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return False