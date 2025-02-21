'''
// Time Complexity :
Problem 1: O(n) as we traverse the entire tree
Problem 2: 
// Space Complexity :
Problem 1: O(n) as we store all the elements in BFS, O(h) in DFS for parsing the tree
Problem 2: 
// Did this code successfully run on Leetcode :
Yes the code ran successfully.
// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
## Problem 1 - Binary Search Tree right side view

## BFS Solution
# Initialize an result array and store the root and its leaf nodes in a FIFO queue. Insert the leaf 
# nodes only when the root is popped from the stack.
# Initialize a size variable to make sure we append all the leaf nodes correctly in the queue.
# For a particular node, if left node is processed, the last element is the righmost and else the first 
# element is the righmost.
# At each level, add the last node in the queue to the result. Return the result array.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root: 
            return result
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if i == n-1:
                    result.append(curr.val)
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
        return result  

## DFS Solution
# Use recursion to traverse the tree.
# Prioritize the right subtree over the left.
# Add the first node encountered at each depth to the result.

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if root == None: return result
        self.dfs(root, 0, result)
        return result

    def dfs(self, root, level, result):
        ##base
        if root == None: return
        ##logic
        if level == len(result):
            result.append(root.val)        
        self.dfs(root.right, level+1, result)
        self.dfs(root.left, level+1, result)

## Problem 2 - Cousins in a binary tree
## BFS Solution
# For BFS using Queue, check whether both x and y are children of the same parent. Return False as they
# are not cousins
# Check whether they are from the same level or not using size variable, and iterate over the size
# Return True if both the elements are found.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if (root == None): return False
        x_found = False; y_found = False
        queue = deque([root])
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if self.areChildren(node, x,y): return False
                if node.val == x: x_found = True
                if node.val == y: y_found = True

                if node.left != None: queue.append(node.left)
                if node.right != None: queue.append(node.right)

            if (x_found and y_found):   return True
            if (x_found or y_found):    return False

        return False
    
    def areChildren(self, root, x, y):
        ## base
        if root == None: return False
        ## logic
        if root.left != None and root.right != None:
            if((root.left.val == x and root.right.val == y) or
                (root.left.val == y and root.right.val == x)):
                return True
        return False
    


