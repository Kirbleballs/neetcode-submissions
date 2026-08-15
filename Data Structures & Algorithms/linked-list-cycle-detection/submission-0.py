# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        counter = 0

        while cur and cur.val <=1000:
            cur.val = 1001 + counter
            counter += 1
            cur = cur.next
        
        if not cur:
            return(False)
        else:
            return(True)

        