# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_one, length_two = 0, 0
        start_one, start_two  = headA, headB
        
        while start_one:
            length_one += 1
            start_one = start_one.next
        while start_two:
            length_two += 1
            start_two = start_two.next
        if length_one >= length_two:
            diff = length_one - length_two
            for _ in range(diff):
                headA = headA.next
        else:
            diff = length_two - length_one
            for _ in range(diff):
                headB = headB.next
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA