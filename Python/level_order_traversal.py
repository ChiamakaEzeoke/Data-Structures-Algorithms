#PROGRAM TO PERFORM LEVEL ORDER TRAVERSAL OF A TREE

import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    ans = []
    if root is None:
        return ans
    queue = collections.deque()
    queue.append(root)

    while queue:
        curr_size = len(queue)
        currList = []

        while curr_size > 0:
            current = queue.popleft()
            currList.append(current.val)
            curr_size -= 1

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        ans.append(currList)
    return ans
        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print (levelOrderTraversal(root))