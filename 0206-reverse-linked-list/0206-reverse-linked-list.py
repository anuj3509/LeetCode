# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iterative approach using two pointers [TC: O(n) ; SC: O(1)]   --> optimal solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next     # temp variable nxt
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# # Recursive approach using two pointers [TC: O(n) ; SC: O(n)]
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         newHead = head  # temp variable to maintain new head initially set the head which is at the current node we are at
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head   # reversing the link b/w the next node and head
#         head.next = None    # if head happens to be the first node, we return Null

#         return newHead