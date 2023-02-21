# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        countHead=head
        count=0
        while countHead:
            count+=1
            countHead=countHead.next
        k=k%count
        if k==0:
            return head
        
        head1=head
        headStart=head
        for _ in range(count-k-1):
            headStart=headStart.next
        temp=headStart.next
        headStart.next=None
        ans=temp
        while temp.next:
            temp=temp.next
        temp.next=head
        return ans
        