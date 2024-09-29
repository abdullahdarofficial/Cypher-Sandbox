# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # def divide(node, p, q):
        #     if p < q:
        #         mid = (p + q) // 2
        #         midNode = node
        #         for _ in range(p, mid):
        #             midNode = node.next
                
        #         divide(node, p, mid)
        #         divide(midnode, mid + 1, q)

        # def merge(left, right):
        #     dummy = ListNode(0)            
        #     while left and right:
        #         if left.val < right.val:
        #             dummy.next = left
        #             left = left.next
        #         else:
        #             dummy.next = right
        #             right = right.next
        #         dummy = dummy.next

        #     if left:
        #         dummy.next = left
        #     if right:
        #         dummy.next = right
                          
        #     return dummy[0]
            

        if not head or not head.next:
            return head

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None
            return head, mid

        def merge(left, right):
            dummy = ListNode(0)
            tail = dummy

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            if right:
                tail.next = right
            return dummy.next
        
        left, right = split(head)

        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)

                

            


            


