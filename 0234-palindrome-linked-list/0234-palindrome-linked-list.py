# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size=0
        head1=head
        while head1:
            size+=1
            head1=head1.next
        prev=None
        lead=head
        half=0
        while half<=size//2-1:
            temp=lead.next
            lead.next=prev
            prev=lead
            lead=temp
            half+=1
        if size%2==1:
            lead=lead.next
        while prev and lead:
            if prev.val==lead.val:
                prev=prev.next
                lead=lead.next
            else:
                return False
        return True
            
        
            
        