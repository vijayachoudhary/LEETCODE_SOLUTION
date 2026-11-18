# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previousNode = None
        currentNode = head

        while currentNode:
            next_Node = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = next_Node

        return previousNode
        