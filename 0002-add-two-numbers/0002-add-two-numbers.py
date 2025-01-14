# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy_head = ListNode(0)  # Create a dummy head for the result linked list
        current = dummy_head  # Pointer to construct the new list
        
        carry = 0  # Initialize carry

        while l1 is not None or l2 is not None or carry:
            # Get the current values, using 0 if the list is exhausted
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit
            
            # Move to the next nodes in the lists and in the result
            current = current.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        return dummy_head.next  # Return the next node of the dummy head, which is the start of the result