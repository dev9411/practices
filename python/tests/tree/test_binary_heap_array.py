import unittest

from tree.binary_heap_array import BinaryHeapArray
from tree.exception.empty_heap_exception import EmptyHeapException


class TestBinaryHeapArray(unittest.TestCase):
    def setUp(self):
        self.heap = BinaryHeapArray()

    def test_empty_heap(self):
        self.assertTrue(self.heap.is_empty())
        
    def test_poping_an_empty_heap(self):
        with self.assertRaises(EmptyHeapException) as context:
            self.heap.pop()
        self.assertEqual(str(context.exception), "Heap is empty")

    def test_peeking_an_empty_heap(self):
        with self.assertRaises(EmptyHeapException) as context:
            self.heap.peek()
        self.assertEqual(str(context.exception), "Heap is empty")
        
    def test_empty_in_non_empty_heap(self):
        self.heap.insert(5)
        self.assertFalse(self.heap.is_empty())
        
    def test_peeking_an_non_empty_heap(self):
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(7)
        self.heap.insert(3)
        self.heap.insert(19)
        self.heap.insert(1)
        self.heap.insert(21)
        self.assertEqual(1, self.heap.peek())

    def test_insert_into_heap(self):
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(7)
        self.heap.insert(3)
        self.heap.insert(19)
        self.heap.insert(1)
        self.heap.insert(21)
        self.assertEqual(self.heap.array, [1, 5, 3, 10, 19, 7, 21])
        
    def test_poping_heap(self):
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(7)
        self.heap.insert(3)
        self.heap.insert(19)
        self.heap.insert(1)
        self.heap.insert(21)
        self.assertEqual(self.heap.pop(), 1)
        self.assertEqual(self.heap.pop(), 3)
        self.assertEqual(self.heap.pop(), 5)
        self.assertEqual(self.heap.pop(), 7)
        self.assertEqual(self.heap.pop(), 10)
        self.assertEqual(self.heap.pop(), 19)
        self.assertEqual(self.heap.pop(), 21)
        self.assertTrue(self.heap.is_empty())
        
        
