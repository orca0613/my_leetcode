# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q = deque()
        q.append(root)
        s = ''
        while q:
            t = q.popleft()
            if t:
                s += str(t.val) + ','
                q.append(t.left)
                q.append(t.right)
            else:
                s += 'null,'
        return s[:-1]
        
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: 
            return []
        
        lst = [0] + list(data.split(','))
        l = len(lst)
        r = t = TreeNode()
        
        def making_tree(tree, n):
            v = lst[n]
            if not v == 'null':
                tree.val = int(v)
            else:
                tree.val = v
            if n * 2 < l:
                tree.left = TreeNode()
                making_tree(tree.left, n * 2)
            if n * 2 + 1 < l:
                tree.right = TreeNode()
                making_tree(tree.right, n * 2 + 1)
        
        making_tree(t, 1)
        return r
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))