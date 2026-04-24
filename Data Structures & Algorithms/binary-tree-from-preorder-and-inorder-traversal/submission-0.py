# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup
        inorder_index = {val: i for i, val in enumerate(inorder)}

        self.pre_index = 0

        def build(left, right):
            # No nodes left in this subtree
            if left > right:
                return None

            # First preorder value is always the root
            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_index[root_val]

            # Build left subtree first, then right subtree
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)