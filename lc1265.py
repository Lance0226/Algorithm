class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        
        tail=None
        while tail!=head:
            curr=head
            while curr.getNext()!=tail:
                curr=curr.getNext()
            tail=curr
            tail.printValue()
