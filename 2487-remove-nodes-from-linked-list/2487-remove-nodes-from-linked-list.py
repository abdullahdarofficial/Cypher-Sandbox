# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        dummy = curr
        dummy.next = head
        nextptr = head

        while dummy.next:
            while nextptr:
                while dummy.next and dummy.next != nextptr and dummy.next.val < nextptr.val:
                    dummy.next = dummy.next.next
                nextptr = nextptr.next
            if dummy.next:
                dummy = dummy.next
                if dummy.next == None:
                    break
                else:
                    nextptr = dummy.next

        return curr.next