# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        currNode = head
        prev = None

        while currNode:
            #save the pointer to next
            nextNode = currNode.next
            #then we can break the reference, and point it to prev
            currNode.next = prev
            #move prev 'forward'
            prev = currNode
            #move curr 'forward
            currNode = nextNode
        
        return prev #because prev ends up being the old tail

