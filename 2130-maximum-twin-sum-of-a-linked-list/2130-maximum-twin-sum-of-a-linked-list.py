# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        back=None
        ahead=ListNode()
        aheadRef=ahead
        curHead=head
        ans=0
        
        length=0
        while curHead:
            ahead.next=ListNode(curHead.val)
            ahead=ahead.next
            
            length+=1
            temp=curHead.next
            curHead.next=back
            back=curHead
            curHead=temp
        aheadRef=aheadRef.next
        for _ in range(length//2):
            ans=max(ans,back.val+aheadRef.val)
            back=back.next
            aheadRef=aheadRef.next
        return ans
        
        
            
        