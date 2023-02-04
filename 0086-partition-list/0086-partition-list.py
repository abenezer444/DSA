# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller=ListNode()
        notSmaller=ListNode()
        small=smaller
        notSmall=notSmaller
        while head:
            if head.val<x:
                smaller.next=head
                smaller=smaller.next
            else:
                notSmaller.next=head
                notSmaller=notSmaller.next
            head=head.next
        smaller.next=notSmall.next
        notSmaller.next=None
        return small.next