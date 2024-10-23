# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = ListNode(0)
        # dummy = curr
        # dummy.next = head
        # nextptr = head

        # while dummy.next:
        #     while nextptr:
        #         while dummy.next and dummy.next != nextptr and dummy.next.val < nextptr.val:
        #             dummy.next = dummy.next.next
        #         nextptr = nextptr.next
        #     if dummy.next:
        #         dummy = dummy.next
        #         if dummy.next == None:
        #             break
        #         else:
        #             nextptr = dummy.next

        # return curr.next


        # Optimize it 

        stack = []
        curr = head

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy
        while stack:
            curr.next = stack.pop(0)
            curr = curr.next

        curr.next = None
        return dummy.next

