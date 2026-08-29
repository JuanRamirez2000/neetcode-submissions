# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        newHead = ListNode()
        dummy = newHead
        
        while head1 and head2:
            if head1.val < head2.val:
                newHead.next = head1
                head1 = head1.next
            else:
                newHead.next = head2
                head2 = head2.next
            newHead = newHead.next
        
        while head1:
            newHead.next = head1
            head1 = head1.next
            newHead = newHead.next
        
        while head2:
            newHead.next = head2
            head2 = head2.next
            newHead = newHead.next
        
        return dummy.next