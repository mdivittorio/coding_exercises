def main():
    node1 = Node(1)
    node1.next = node2 = Node(5)
    node2.next = node3 = Node(10)
    lis = LinkedList()
    lis.head = node1
    print(lis)
    lis.delete_val(1)
    print(lis)
    lis2 = LinkedList.get_linked_list(1, 7, 3, 8)
    print(lis2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}]'


class LinkedList:
    def __init__(self):
        self.head = None

    @classmethod
    def get_linked_list(cls, *values):
        ll = LinkedList()
        for val in values:
            ll.add(val)
        return ll

    def __len__(self):
        pass

    def __str__(self):
        lis = ''
        current = self.head
        while current:
            if current == self.head:
                lis = lis + str(current)
            else:
                lis = lis + '-->' + str(current)
            current = current.next
        return lis

    def add(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current:
                if not current.next:
                    current.next = node
                    return
                else:
                    current = current.next

    def delete_val(self, val):
        if not self:
            return
        follow = None
        if not self.head.next:  # only one item in list
            if self.head.data == val:
                self.head = None
                return
        else:
            # keep ref to previous node to update next pointer
            current = self.head
            while current:
                if current.data == val:
                    if current != self.head:
                        follow.next = current.next
                        current = follow.next
                    else:
                        self.head = current = current.next
                else:
                    follow = current
                    current = current.next

    def delete_index(self, index):
        pass

    def remove_duplicates(self):
        pass

    def merge_sort(self):
        pass




main()
