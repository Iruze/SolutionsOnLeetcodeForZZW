class Node:
    # 定义链表
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        # 链表长度
        self.size = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val)
        new_head.next, self.head = self.head, new_head
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            node = self.head
            while node and node.next:
                node = node.next
            node.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size: return
        elif index == self.size: self.addAtTail(val)
        elif index <= 0: self.addAtHead(val)
        else:
            node = self.head
            while index > 1:
                node = node.next
                index -= 1
            new_node = Node(val)
            node.next, new_node.next = new_node, node.next
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.size:
            dummy = Node(-1)
            dummy.next = self.head
            node = dummy
            while index:
                node = node.next
                index -= 1
            node.next = node.next.next
            self.head = dummy.next
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
