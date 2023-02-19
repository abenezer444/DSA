# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        oddHead=ListNode()
        ans=oddHead
        
        evenHead=ListNode()
        evenTemp=evenHead
        parity=1
        while temp:
            if parity%2==1:
                
                oddHead.next=temp
                oddHead=oddHead.next
            else:
                evenHead.next=temp
                evenHead=evenHead.next
            parity+=1
            temp=temp.next
        evenHead.next=None
        oddHead.next=evenTemp.next
        
        return ans.next
        
        