# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        val = []
        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next

        reversed_val = val[::-1] 

        if val == reversed_val:
            return True   
        else:
            return False    
