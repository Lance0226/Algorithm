"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        dlist = {}
        pointer = head
        
        while pointer:
            dlist[pointer] = Node(pointer.val, None, None)
            pointer = pointer.next
        
        
        pointer = head
        while pointer:
            if pointer.random:
                dlist[pointer].random = dlist[pointer.random]
            if pointer.next:
                dlist[pointer].next = dlist[pointer.next]
            pointer = pointer.next
        
        
        return dlist[head]
        
            
