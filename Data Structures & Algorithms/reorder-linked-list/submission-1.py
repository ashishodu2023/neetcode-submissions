# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        #1.Find the middle
        slow = head
        fast = head 
        previous = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is the middle

        #2.Detach first half from the list 
        second = slow.next
        slow.next = None 

        #3.Reverse the other half
        current = second
        while current:
            nxt = current.next
            current.next = previous
            previous = current 
            current = nxt
        
        #4.Merge the node alternatively 
        first = head
        second = previous
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second 
            second.next = first_next

            first = first_next
            second = second_next
            