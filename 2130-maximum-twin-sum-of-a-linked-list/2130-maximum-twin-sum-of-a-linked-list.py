# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head or not head.next:
            return 0
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.first = head
        self.maxsum = 0
        # while second:
        #     maxsum = max(maxsum, first.val + second.val)
        #     first = first.next
        #     second = second.next

        # return maxsum

        def recursive(second):
            if not second:
                return
            recursive(second.next)
            self.maxsum = max((self.first.val + second.val ), self.maxsum)
            self.first = self.first.next
        
        recursive(slow)
        return self.maxsum





        
        