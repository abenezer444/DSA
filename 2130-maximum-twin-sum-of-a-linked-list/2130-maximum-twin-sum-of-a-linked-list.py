# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        back=None
        while fast and fast.next:
            
            fast=fast.next.next
            
            temp=slow.next
            slow.next=back
            back=slow
            slow=temp
        ans=0
        
        while back:
            ans=max(ans,back.val+slow.val)
            back=back.next
            slow=slow.next
        return ans
            
            