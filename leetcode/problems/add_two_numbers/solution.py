# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1
        carry = 0
        while l1 and l2:
            prev = l1
            carry, l1.val = divmod(l1.val+l2.val+carry, 10)
            l1, l2 = l1.next, l2.next
        
        tail = l1 or l2
        prev.next = tail

        while tail:
            carry, tail.val = divmod(carry+tail.val, 10)
            prev, tail = tail, tail.next
        else:
            if carry:
                prev.next = ListNode(1)
        
        return res

