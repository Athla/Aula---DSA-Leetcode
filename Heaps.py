from typing import override


class MinHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self) -> int | None:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index: int) -> None:
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
        return str(self.heap)


class MaxHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> int | None:
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index: int) -> None:
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
        return str(self.heap)
