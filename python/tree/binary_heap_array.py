from tree.exception.empty_heap_exception import EmptyHeapException


class BinaryHeapArray:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def pop(self):
        if self.is_empty():
            raise EmptyHeapException("Heap is empty")

        if len(self.array) == 1:
            return self.array.pop()

        min_item = self.peek()
        self.array[0] = self.array.pop()
        self.__bubble_down(0)
        return min_item

    def peek(self):
        if self.is_empty():
            raise EmptyHeapException("Heap is empty")
        return self.array[0]

    def insert(self, value: int):
        return self.__insert_at(value, len(self.array))

    def __insert_at(self, value: int, insert_at: int):
        if insert_at == 0:
            return self.__put_to_array(0, value)
        
        parent_index = self.__parent_of(insert_at)
        if self.array[parent_index] <= value:
            return self.__put_to_array(insert_at, value)

        self.__put_to_array(insert_at, self.array[parent_index])
        self.__insert_at(value, parent_index)

    def __parent_of(self, index: int) -> int:
        if index % 2 == 0:
            return index//2 - 1
        return index//2

    def __bubble_down(self, index: int):
        next_index = self.__next_bubble_index(index)
        if next_index == -1 or next_index >= len(self.array):
            return

        if self.array[next_index] < self.array[index]:
            tmp = self.array[index]
            self.array[index] = self.array[next_index]
            self.array[next_index] = tmp
            return self.__bubble_down(next_index)

        return
    
    def __next_bubble_index(self, index: int) -> int:
        (child1, child2) = self.__children_of(index)
        if child1 >= len(self.array):
            return -1
        if child2 >= len(self.array):
            return child1
        return child1 if self.array[child1] < self.array[child2] else child2

    def __children_of(self, index: int) -> list:
        return (
            index * 2 + 1,
            index * 2 + 2
        )

    def __put_to_array(self, index, value):
        if index == len(self.array):
            return self.array.append(value)
        self.array[index] = value

