# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.random = 0

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if not self.head:
            return -float('Inf')
        node = self.head
        i = 1
        while node:
            # randint(1, i)的范围为 [1, i]
            if random.randint(1, i) == 1:
                self.random = node.val
            i += 1
            node = node.next
        return self.random



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
