# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0

        # in-place calculation of the number i.e.,
        # for each node, multiply current number by 2 and add node's value
        while head:
            num = num * 2 + head.val
            head = head.next
        return num

        # TC: O(n) ; SC: O(1)