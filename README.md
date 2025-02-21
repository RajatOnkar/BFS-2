# BFS-2

## Problem 1

Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)

## BFS Solution
# Initialize an result array and store the root and its leaf nodes in a FIFO queue. Insert the leaf 
# nodes only when the root is popped from the stack.
# Initialize a size variable to make sure we append all the leaf nodes correctly in the queue.
# For a particular node, if left node is processed, the last element is the righmost and else the first 
# element is the righmost.
# At each level, add the last node in the queue to the result. Return the result array.

## DFS Solution
# Use recursion to traverse the tree.
# Prioritize the right subtree over the left.
# Add the first node encountered at each depth to the result.

## Problem 2

Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)

## BFS Solution
# For BFS using Queue, check whether both x and y are children of the same parent. Return False as they
# are not cousins
# Check whether they are from the same level or not using size variable, and iterate over the size
# Return True if both the elements are found.


