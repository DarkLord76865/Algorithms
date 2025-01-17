## Binary search tree

**Binary search tree** (BST), also called an ordered or sorted binary tree,
is a rooted binary tree data structure with the key of each internal node being
greater than all the keys in the respective node's left subtree and less than
the ones in its right subtree. The time complexity of operations on the
binary search tree is linear with respect to the height of the tree.

Binary search trees allow binary search for fast lookup, addition, and removal
of data items. Since the nodes in a BST are laid out so that each comparison skips
about half of the remaining tree, the lookup performance is proportional to that of
binary logarithm. BSTs were devised in the 1960s for the problem of efficient storage
of labeled data and are attributed to Conway Berners-Lee and David Wheeler.

The performance of a binary search tree is dependent on the order of insertion
of the nodes into the tree since arbitrary insertions may lead to degeneracy;
several variations of the binary search tree can be built with guaranteed
worst-case performance. The basic operations include: search, traversal, insert and delete.
BSTs with guaranteed worst-case complexities perform better than an unsorted array,
which would require linear search time.

The complexity analysis of BST shows that, on average, the insert, delete and search
takes $O(\log n)$ for $n$ nodes. In the worst case, they degrade to that of a
singly linked list: $O(n)$. To address the boundless increase of the tree height
with arbitrary insertions and deletions, self-balancing variants of BSTs are introduced
to bound the worst lookup complexity to that of the binary logarithm.
AVL trees were the first self-balancing binary search trees, invented in 1962 by
Georgy Adelson-Velsky and Evgenii Landis.

Binary search trees can be used to implement abstract data types such as dynamic sets,
lookup tables and priority queues, and used in sorting algorithms such as tree sort.
