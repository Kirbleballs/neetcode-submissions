# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if not cur1:
            return cur2
        
        if not cur2:
            return cur1

        if cur1.val < cur2.val:
            head = cur1
            cur = head
            cur1 = cur1.next
        else:
            head = cur2
            cur = head
            cur2 = cur2.next
        
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        
        if cur1 == None:
            cur.next = cur2
        if cur2 == None:
            cur.next = cur1
        
        return(head)

                
                













        