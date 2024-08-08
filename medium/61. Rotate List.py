# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
from collections import deque

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        q = deque()

        while head:
            q.append(head.val)
            head = head.next
        q.rotate(k % len(q))

        ret = t = ListNode()
        while q:
            t.val = (q.popleft())
            if q:
                t.next = ListNode()
                t = t.next
        
        return ret