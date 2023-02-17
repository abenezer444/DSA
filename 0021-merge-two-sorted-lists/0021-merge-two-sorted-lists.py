# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedHead=ListNode()
        ans=mergedHead
        while list1 and list2:
            if list1.val<=list2.val:
                mergedHead.next=list1
                mergedHead=mergedHead.next
                list1=list1.next
            else:
                mergedHead.next=list2
                mergedHead=mergedHead.next
                list2=list2.next
        if list1:
            mergedHead.next=list1
        if list2:
            mergedHead.next=list2
        return ans.next

            
        
        