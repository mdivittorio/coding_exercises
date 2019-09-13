from coding_exercises.CodingInterview.utils.stack import Stack
from coding_exercises.CodingInterview.utils.node import StackNode


class StackList:
    def __init__(self, threshold: int):
        self.stacks = None
        self.threshold = threshold

    def __str__(self):
        sl_str = '<<'
        if self.stacks:
            for index, stack in enumerate(self.stacks):
                sl_str = sl_str + f'S{index+1}::' + str(stack)
        return sl_str + '>>'

    def push(self, data: int):
        pushed = False
        if self.stacks:
            for stack in self.stacks:
                if not stack.at_capacity(self.threshold):
                    pushed = True
                    stack.push(data)
                    break
        else:
            self.stacks = []

        if not pushed:
            new_stack = Stack()
            new_stack.push(data)
            self.stacks.append(new_stack)

    def pop(self) -> StackNode:
        if self.stacks:
            for index, stack in reversed(list(enumerate(self.stacks))):
                if stack.is_empty():
                    self.stacks.pop(index)
            return self.stacks[-1].pop()
        else:
            return None

    def pop_at(self, index) -> StackNode:
        if self.stacks:
            try:
                return self.stacks[index].pop()
            except IndexError:
                return None
