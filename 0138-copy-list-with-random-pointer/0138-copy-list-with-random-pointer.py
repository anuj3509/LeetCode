"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = { None : None } # none:none is for an edge case if pointer is pointing to NULL

        # First pass - cloning the LL node and adding to hashmap. Not conecting pointers
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next

        # Second pass - connecting links
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next

        return oldtocopy[head]