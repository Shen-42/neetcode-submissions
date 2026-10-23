# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first_half = head
        second_half = prev

        while first_half and second_half:
            next_first = first_half.next
            next_second = second_half.next

            first_half.next = second_half
            second_half.next = next_first

            first_half = next_first
            second_half = next_second

