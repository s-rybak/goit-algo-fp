class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the linked list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """
        Inserts a new node after a given node.
        """
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """
        Deletes a node with the given key.
        """
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """
        Searches for a node with the given data.
        """
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        """
        Prints the linked list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        """
        Reverses the linked list.
        """
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def merge(self, left, right):
        """
        Merges two sorted linked lists.
        """
        merged_list = LinkedList()

        while left and right:
            if left.data <= right.data:
                merged_list.insert_at_end(left.data)
                left = left.next
            else:
                merged_list.insert_at_end(right.data)
                right = right.next

        while left:
            merged_list.insert_at_end(left.data)
            left = left.next

        while right:
            merged_list.insert_at_end(right.data)
            right = right.next

        return merged_list.head

    def sort_list(self):
        """
        Sorts the linked list using merge sort.
        """
        if not self.head or not self.head.next:
            return

        def get_middle(head):
            """
            Gets the middle of the linked list.
            """
            if not head:
                return None
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge_sort(head):
            """
            Sorts the linked list using merge sort.
            """
            if not head or not head.next:
                return head

            middle = get_middle(head)
            right = middle.next
            middle.next = None

            return self.merge(merge_sort(head), merge_sort(right))

        self.head = merge_sort(self.head)


llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(2)
llist.insert_at_end(4)
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(6)
llist.print_list()

llist.reverse_list()
print("Reversed list:")
llist.print_list()

llist.sort_list()
print("Sorted list:")
llist.print_list()
