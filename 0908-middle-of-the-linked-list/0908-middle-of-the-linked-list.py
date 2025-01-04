# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# The concept here is "Loop unrolling". The number of comparsion controlling the loop is 
# actually just a 1/3 of the naive solution (traversing the list and get its length and then 
# return the length). However, It's a space time trade off. You need some extra memory and k 
# extra operations in the for loop  for controlling second pointer.