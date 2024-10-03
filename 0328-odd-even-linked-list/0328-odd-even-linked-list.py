# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        half = ListNode(0)
        dummy = half
        node = head
        prev = None
        while node:
            if node.next:
                dummy.next = node.next
                node.next = node.next.next
                dummy = dummy.next
                dummy.next = None
            prev = node
            node = node.next
            
        prev.next = half.next
        return head
            




        