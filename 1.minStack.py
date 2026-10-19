import subprocess
subprocess.run('cls', shell=True)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


minStack = MinStack()

minStack.push(5)
minStack.push(3)
minStack.push(7)

print("Stack:", minStack.stack)
print("Minimum Stack:", minStack.min_stack)
print("Minimum:", minStack.getMin())

minStack.pop()

print("After pop:")
print("Stack:", minStack.stack)
print("Minimum Stack:", minStack.min_stack)
print("Top:", minStack.top())
print("Minimum:", minStack.getMin())
