# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # keep cutting the num. of lists in half until we reach only one LL
        while len(lists) > 1:
            combinedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                combinedLists.append(self.mergeList(l1, l2))
            lists = combinedLists
        return lists[0]


    # Function to merge 2 LL [Leetcode 21]
    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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