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
        mappings = {}
        current = head

        while current:
            mappings[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copy = mappings[current]
            
            copy.next = mappings.get(current.next)
            copy.random = mappings.get(current.random)

            current = current.next
        
        return mappings.get(head)


