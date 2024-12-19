# Trees and BFS & DFS
- Trees are, basically, acyclic graphs, and have many different implementations that fall under the category of a tree.
- That being said, generally, the methods to traverse a tree are oftenly the same, and they are:
    - Breadth First Search (BFS)
    - Depth First Search (DFS)

## Breath First Search (BFS - Pesquisa em Largura)
- In this method, instead of going down one path until the end, we explore it via layers. It's possible to think of it as a waves that show what you have explored so far.
- The algorithm is as follows:
    1. Create a queue and add the root node to it.
    2. While the queue is not empty, do:
        1. Remove the first node from the queue.
        2. Add all of its children to the queue.
        3. Do something with the node.
- The time complexity of this algorithm is O(V + E), being it the number of Vertices and Edges in the Graph.
- A fun fact, since it uses a queue, it's possible to see that the nodes are visited in the order they were added to the tree.


## Depth First Search (DFS - Pesquisa em Profundidade)
- In this method, we go down one path until the end, and then we backtrack to the previous node and go down another path.
- The algorithm implementation using a stack is as follows:
    1. Create a stack and add the root node to it.
    2. While the stack is not empty, do:
        1. Remove the first node from the stack.
        2. Add all of its children to the stack.
        3. Do something with the node.
- The algorithm implementation using recursion is as follows:
    1. Do something with the node.
    2. For each child of the node, do:
        1. Call the function recursively.
- The time complexity of this algorithm is O(n), where n is the number of nodes in the tree. Or the number of vertices in the graph.
- A fun fact, since it uses a stack, it's possible to see that the nodes are visited in the reverse order they were added to the tree.


# Helpful Leetcodes to solve:
## BFS
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

## DFS
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) 
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

