from typing import override


class MinHeap:
    """
    A MinHeap implementation that maintains integers in a heap data structure
    where the parent node is always smaller than its children.
    The heap is represented internally as a list.
    """

    def __init__(self) -> None:
        """
        Initialize a new MinHeap.
        The heap is represented as a list of integers.
        """
        self.heap: list[int] = []

    def insert(self, value: int) -> None:
        """
        Insert a new integer into the heap and maintain the heap property.

        Args:
            value (int): The integer value to be inserted into the heap.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self) -> int | None:
        """
        Remove and return the smallest integer from the heap.
        After extraction, the heap property is maintained.

        Returns:
            int | None: The smallest integer in the heap, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index: int) -> None:
        """
        Ensure the heap property is maintained after insertion by moving
        the element at the given index up the heap until it's in the correct position.

        Args:
            index (int): The index of the element to move up in the heap.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index: int) -> None:
        """
        Ensure the heap property is maintained after extraction by moving
        the element at the given index down the heap until it's in the correct position.

        Args:
            index (int): The index of the element to move down in the heap.
        """
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self._heapify_down(smallest)

    @override
    def __str__(self) -> str:
        """
        Return a string representation of the heap.

        Returns:
            str: The string representation of the heap list.
        """
        return str(self.heap)


class MaxHeap:
    """
    A MaxHeap implementation that maintains integers in a heap data structure
    where the parent node is always larger than its children.
    The heap is represented internally as a list.
    """

    def __init__(self) -> None:
        """
        Initialize a new MaxHeap.
        The heap is represented as a list of integers.
        """
        self.heap: list[int] = []

    def insert(self, value: int) -> None:
        """
        Insert a new integer into the heap and maintain the heap property.

        Args:
            value (int): The integer value to be inserted into the heap.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> int | None:
        """
        Remove and return the largest integer from the heap.
        After extraction, the heap property is maintained.

        Returns:
            int | None: The largest integer in the heap, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index: int) -> None:
        """
        Ensure the heap property is maintained after insertion by moving
        the element at the given index up the heap until it's in the correct position.

        Args:
            index (int): The index of the element to move up in the heap.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index: int) -> None:
        """
        Ensure the heap property is maintained after extraction by moving
        the element at the given index down the heap until it's in the correct position.

        Args:
            index (int): The index of the element to move down in the heap.
        """
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index],
            )
            self._heapify_down(largest)

    @override
    def __str__(self) -> str:
        """
        Return a string representation of the heap.

        Returns:
            str: The string representation of the heap list.
        """
        return str(self.heap)
