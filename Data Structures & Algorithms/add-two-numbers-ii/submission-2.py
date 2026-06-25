# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1,stack2=[],[]

        while l1:
            stack1.append(l1.val)
            l1 = l1.next 
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next 
        
        carry = 0 
        head = None 

        while stack1 or stack2 or carry :
            num1 = stack1.pop() if stack1 else 0 
            num2 = stack2.pop() if stack2 else 0 

            total = carry + num1 + num2
            carry = total //10 
            digit = total %10

            node = ListNode(digit)
            node.next = head 
            head = node

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
            

        return head
