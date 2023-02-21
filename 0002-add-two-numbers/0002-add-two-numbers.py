# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        rem = []
        
        while l1 and l2:
            carry = rem.pop() if rem else 0
            stack.append((l1.val+l2.val+carry)%10)
            if (l1.val+l2.val+carry)//10 == 1:
                rem.append(1)
            l1 = l1.next
            l2 = l2.next
        while l1:
            carry = rem.pop() if rem else 0
            stack.append((l1.val + carry)%10)
            if(l1.val + carry)//10:
                rem.append(1)
            l1 = l1.next
        while l2:
            carry = rem.pop() if rem else 0
            stack.append((l2.val + carry)%10)
            if(l2.val + carry)//10:
                rem.append(1)
            l2 = l2.next
        stack.extend(rem)
        dummy = ListNode()
        tail = dummy
        for num in stack:
            tail.next = ListNode(num)
            tail = tail.next
        return dummy.next
        
                