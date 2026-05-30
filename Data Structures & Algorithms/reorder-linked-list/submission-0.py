# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        #Find the middle node
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second half
        previous = None 
        current = slow.next
        slow.next = None 

        while current:
            nxt = current.next
            current.next = previous
            previous = current 
            current = nxt

        #Merge the 2halves 
        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

