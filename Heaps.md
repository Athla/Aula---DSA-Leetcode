# MinHeaps and What they are
- It's a "Tree-Like" structure were the parent node can be smaller (when it's a MinHeap) or bigger (when it's a MaxHeap) than its children.
- It's often used to implemente Priority Queues and similar systems where the weight will determine the order of execution.
- The main operatiosn that a Heap will implement are:
    - Insert
    - Extract Min/Max
- To achieve those methods, it uses helper methods such as:
    - Heapfiy Up/Down -> To maintain the Heap property
    - Get Parent/Left/Right -> To navigate the tree

# Helpful Leetcodes to solve:
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
