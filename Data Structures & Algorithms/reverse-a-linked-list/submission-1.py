# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = ListNode()
        prevNode = None 
        while head:
           nextNode = head.next # store next in a new pointer
           head.next = prevNode # change current head to point to prev
           prevNode = head # update prev to be current 
           head = nextNode #update current to be next 
        return prevNode


