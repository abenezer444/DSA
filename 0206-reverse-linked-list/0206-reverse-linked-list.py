# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        ahead=head
        while ahead:
            temp=ahead.next
            ahead.next=prev
            prev=ahead
            ahead=temp
        return prev
            
        