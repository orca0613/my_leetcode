# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        storage = []
        while head:
            storage.append(head.val)
            head = head.next
        t = len(storage) - n
        
        answer = r = ListNode()
        for i in range(len(storage)):
            if i != t:
                r.next = ListNode(storage[i])
                r = r.next
        return answer.next
        