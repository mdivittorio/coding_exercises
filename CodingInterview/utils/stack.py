from coding_exercises.CodingInterview.utils.node import StackNode


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        current = self.top
        stack_str = '{'
        while current:
            formatted_node = f'[{current.data}]' if current == self.top else f'==>[{current.data}]'
            stack_str = stack_str + formatted_node
            current = current.next
        return stack_str + '}'

    def pop(self) -> StackNode:
        if self.top:
            top_node = self.top
            self.top = self.top.next
        else:
            top_node = None
        return top_node

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def at_capacity(self, cap) -> bool:
        count = 0
        current = self.top
        while current:
            count += 1
            if count == cap:
                return True
            current = current.next
        return False

    def is_empty(self):
        return self.top is None
