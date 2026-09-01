# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow is the last position of the left half
        # Then we reverse the right half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next


        # Merge the two halves
        first, second = head, prev
        while second: 
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next