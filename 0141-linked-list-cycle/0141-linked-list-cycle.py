# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # # Using a set to track visited nodes [TC = SC = O(n)]
        # visited = set()    # set
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False

        # Using fast and slow pointers [TC = O(n), SC = O(1)]
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
         