from dataclasses import dataclass
from typing import Optional

class StackNode:
    def __init__(self, data: int, next: Optional['StackNode'] = None):
        self.data = data
        self.next = next
    
@dataclass
class StackV1:
    top: StackNode

    def is_empty(self):
        return True if self.top is None else False

    def push(self, data):
        node = StackNode(data=data, next=self.top)
        self.top = node
        
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        remove = self.top
        self.top = self.top.next
        return remove
            
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top
        