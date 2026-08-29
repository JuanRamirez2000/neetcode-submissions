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
            #Incremenent 1 twice as fast
            curr = curr.next
            faster = faster.next.next

            # If this is ever None then there is no cycle
            if faster == None:
                return False

            #If they equal to each other then there is a cycle
            if curr == faster:
                return True

        #Guranteed to be false
        return False 