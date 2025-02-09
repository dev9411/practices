import unittest
from stack.stack_v1 import StackV1

class TestStackV1(unittest.TestCase):
    def setUp(self):
        """Initialize a stack for testing."""
        self.stack = StackV1(top=None)

    def test_is_empty(self):
        """Test is_empty() on an empty stack."""
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_after_push(self):
        """Test is_empty() after pushing an element."""
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_push_and_peek(self):
        """Test push() and peek()."""
        self.stack.push(10)
        self.assertEqual(self.stack.peek().data, 10)

    def test_push_multiple_elements(self):
        """Test pushing multiple elements."""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek().data, 20)

    def test_pop(self):
        """Test pop() on a non-empty stack."""
        self.stack.push(10)
        self.stack.push(20)
        popped_node = self.stack.pop()
        self.assertEqual(popped_node.data, 20)
        self.assertEqual(self.stack.peek().data, 10)

    def test_pop_empty_stack(self):
        """Test pop() on an empty stack."""
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_peek_empty_stack(self):
        """Test peek() on an empty stack."""
        with self.assertRaises(ValueError):
            self.stack.peek()

    def test_push_pop_combination(self):
        """Test a combination of push() and pop()."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()
        self.stack.push(30)
        self.assertEqual(self.stack.peek().data, 30)
        self.stack.pop()
        self.assertEqual(self.stack.peek().data, 10)

    def test_pop_all_elements(self):
        """Test popping all elements until the stack is empty."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_peek_after_pop(self):
        """Test peek() after popping an element."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()
        self.assertEqual(self.stack.peek().data, 10)

if __name__ == "__main__":
    unittest.main()