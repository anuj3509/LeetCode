# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:   # if list 2 <= list 1
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if you reach the end of LL, just append the remaining part o
        if list1:  # if list1 is not null
            tail.next = list1
        elif list2:    # else if l2 is not null
            tail.next = list2

        return dummy.next