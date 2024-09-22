# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not head or not head.next:
#             return head

#         dummy = ListNode(0)
#         dummycurr = dummy
#         prev = head
#         curr = head.next
#         flag = False
#         while curr:
#             if prev.val != curr.val:
#                 if flag:
#                     flag = False
#                 else:
#                     dummycurr.next = ListNode(prev.val)
#                     dummycurr = dummycurr.next
#             else:
#                 flag = True
#             prev = curr
#             curr = curr.next
        
#         if dummycurr.val != prev.val and flag == False:
#             dummycurr.next = ListNode(prev.val)
        
#         return dummy.next
                    

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy_curr = dummy
        prev = head
        curr = head.next
        has_duplicates = False

        while curr:
            if prev.val == curr.val:
                has_duplicates = True
            else:
                if not has_duplicates:
                    dummy_curr.next = ListNode(prev.val)
                    dummy_curr = dummy_curr.next
                has_duplicates = False
            prev = curr
            curr = curr.next

        # Check the last node
        if not has_duplicates:
            dummy_curr.next = ListNode(prev.val)

        return dummy.next
