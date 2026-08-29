# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        faster = head
        while faster.next != None:
            curr = curr.next
            faster = faster.next.next
            if faster == None:
                return False
            if curr == faster:
                return True
        return False 