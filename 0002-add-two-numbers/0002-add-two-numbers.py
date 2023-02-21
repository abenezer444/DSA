# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def createNode(val):
            return ListNode(val)
        pre1=ListNode(0,l1)
        pre2=ListNode(0,l2)
        
        ans=ListNode()
        ref, carry,prevRaw =ans, 0,0
        while l1 and l2:
            carry=1 if prevRaw>9 else 0
            raw=l1.val+l2.val+carry
            # carry = 0
            if raw>9:
                node=createNode(raw%10)
            else:
                node=createNode(raw)
            l1=l1.next
            l2=l2.next
            pre1=pre1.next
            pre2=pre2.next
            ans.next=node
            ans=ans.next
            carry=1 if raw>9 else 0
            prevRaw = raw


        while l1:
            raw = 0
            if carry:
                raw =carry
            raw +=l1.val
            carry = 1 if raw > 9 else 0
            if raw>9:
                node=createNode(raw%10)
            else:
                node=createNode(raw)
            l1=l1.next
            ans.next=node
            ans=ans.next
        while l2:
            raw = 0
            if carry:
                raw =carry
            
            raw +=l2.val
            carry = 1 if raw > 9 else 0
            if raw>9:
                node=createNode(raw%10)
            else:
                node=createNode(raw)
            l2=l2.next
            ans.next=node
            ans=ans.next
        if carry:
            node=createNode(1)
            ans.next=node
            ans=ans.next
            
            
            
            
        return ref.next
                