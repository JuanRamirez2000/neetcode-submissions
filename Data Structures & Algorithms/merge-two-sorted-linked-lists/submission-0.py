# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = finalList = ListNode()

        while list1 and list2:
            # if list 1 is lower
            # set final pointer to it and increment list 1
            if list1.val < list2.val:
                finalList.next = list1
                list1 = list1.next

            # if list 2 is lower
            # set final pointer to it and increment by 1
            else:
                finalList.next = list2
                list2 = list2.next

            # this is so we dont overwrite anything and increment the final list by 1
            finalList = finalList.next
        
        # grab the remaining part of the list since list1 and list2 can be different lengths
        finalList.next = list1 or list2

        #this is so we can avoid the value = 0 from the ListNode class initialization
        return dummy.next
