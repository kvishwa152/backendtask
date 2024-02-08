#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2. Given the root of an n-ary tree, print the postorder traversal of its nodes'values.


# In[2]:


from typing import List

class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    @staticmethod
    def createTree(input: List[int]) -> Node:
        if not input:
            return None

        nodes = {i: Node(val=i) for i in range(len(input))}
        root = None

        try:
            for i, val in enumerate(input):
                if val is not None:
                    if nodes[i].val is None:
                        nodes[i].val = val
                    else:
                        nodes[i].val = val

                    if not root:
                        root = nodes[i]

                    for child_index in range(i + 1, i + val + 1):
                        if child_index < len(input) and input[child_index] is not None:
                            nodes[i].children.append(nodes[child_index])
        except IndexError:
            print("Invalid input format. Unable to create tree.")
            return None

        return root

    @staticmethod
    def traverseTree(root: Node) -> None:
        if not root:
            return

        try:
            for child in root.children:
                Solution.traverseTree(child)
        except AttributeError:
            print("Invalid tree structure.")
            return

        print(root.val, end=' ')

# Example usage
input_example = [1, None, 3, 2, 4, None, 5, 6]
root_node = Solution.createTree(input_example)
if root_node:
    Solution.traverseTree(root_node)


# In[ ]:


#1. Given an Nary-Tree input serialisation which represents the level ordertraversal of a tree. Each group of children is separated by the None value (Seeexamples). The task is to create a tree from this input and return the root nodeof the same.


# In[ ]:


from typing import List

class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    @staticmethod
    def createTree(input: List[int]) -> Node:
        try:
            if not input:
                return None

            root = Node(input[0])
            stack = [root]
            i = 1

            while stack and i < len(input):
                if input[i] is None:
                    stack.pop()
                else:
                    current_node = Node(input[i])
                    stack[-1].children.append(current_node)
                    stack.append(current_node)
                i += 1

            return root
        except Exception as e:
            print(f"Error in createTree: {e}")
            return None

    @staticmethod
    def traverseTree(root: Node) -> List[int]:
        try:
            if not root:
                return []

            result = []
            stack = [root]

            while stack:
                current_node = stack.pop()
                result.append(current_node.val)
                stack.extend(reversed(current_node.children))

            return result
        except Exception as e:
            print(f"Error in traverseTree: {e}")
            return []

# Example usage
input_data = [1, None, 3, 2, 4, None, 5, 6]

try:
    root = Solution.createTree(input_data)
    output = Solution.traverseTree(root)
    print("Traversal Output:", output)
except Exception as e:
    print(f"Error: {e}")

