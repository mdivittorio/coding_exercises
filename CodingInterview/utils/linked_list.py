class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}]'


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

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

    @classmethod
    def get_linked_list(cls, *values):
        ll = cls()
        for val in values:
            ll.add(val)
        return ll

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
        current = self.head
        prev = None
        while current:
            if current.data == val:
                if prev:
                    prev.next = current.next
                else:   # no previous node => matching head
                    self.head = current.next
                return
            else:
                prev = current
                current = current.next

    def delete_index(self, index):
        adj_index = index if index >= 0 else index + len(self)
        if not self.head:
            return
        elif adj_index == 0:
            self.head = self.head.next
        else:
            if adj_index > len(self) - 1:
                raise IndexError(f'Index {index} is outside bounds of linked list.')
            current = self.head
            for i in range(adj_index-1):     # traverse to node behind one to be removed
                current = current.next
            current.next = current.next.next

    def remove_duplicates(self):
        current = self.head
        while current:
            matches = len(self.find(current.data))
            for i in range(matches-1):
                indices = self.find(current.data)
                self.delete_index(indices[1])   # keep first match
            current = current.next

    def find(self, value):
        index = 0
        current = self.head
        index_matches = []
        while current:
            if current.data == value:
                index_matches.append(index)
            index += 1
            current = current.next
        return index_matches

    def reverse_list(self):
        if not self.head:
            return
        follow = self.head
        current = follow.next
        while current:
            if follow == self.head:
                follow.next = None
            tmp = current.next
            current.next = follow
            follow = current
            current = tmp
        self.head = follow
