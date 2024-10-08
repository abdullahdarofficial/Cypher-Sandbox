# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # if not head or not head.next:
        #     return head
        
        # prev = head
        # curr = head.next

        # indexFound = True
        # indexPtr = None

        # while curr:
        #     if curr.val >= x and indexFound:
        #         indexPtr = prev
        #         indexFound = False
        #         prev = curr
        #         curr = prev.next
        #     elif curr.val < x:
        #         prev = curr
        #         ptr_next_node = indexPtr.next
        #         curr_next_node = curr.next
        #         indexPtr.next = curr
        #         curr.next = ptr_next_node
        #         indexPtr = indexPtr.next
        #         curr = curr_next_node
        #     else:
        #         prev = curr
        #         curr = prev.next


        # return head

        if not head:
            return head

        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next