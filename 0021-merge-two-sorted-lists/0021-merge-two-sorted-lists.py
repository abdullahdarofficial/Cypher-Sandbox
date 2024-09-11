# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # p1 = list1
        # p2 = list2
       

        # if p1.val <= p2.val:
        #     l = p3 = p1
        #     p1 = p1.next
        # else:
        #     l = p3 = p2
        #     p2 = p2.next

        # while p1 and p2:

        #     if p1.val <= p2.val:
        #         p3.next = p1
        #         p3 = p3.next
        #         p1 = p1.next
        #     else:
        #         p3.next = p2
        #         p3 = p3.next
        #         p2 = p2.next

        # while p1:
        #     p3.next = p1
        #     p1 = p1.next
        #     p3 = p3.next
        # while p2:
        #     p3.next = p2
        #     p2 = p2.next
        #     p3 = p3.next

        # return l


        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next