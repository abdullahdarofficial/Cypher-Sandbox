# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         if head is None:
#             return head

#         current = head
#         count = 0

#         while current:
#             current = current.next
#             count += 1
#         k%=count

#         while k > 0:
#             current = head
#             prev = current
#             while current.next:
#                 prev = current
#                 current = current.next
            
#             current.next = head
#             head = current
#             prev.next = None

#             k-=1

#         return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        k %= length

        if k == 0:
            return head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None
        current.next = head

        return new_head
