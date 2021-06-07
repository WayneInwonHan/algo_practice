def isValidBST(self, root):
    return self._isValidBST(root, -2147483647, 2147483647);

def _isValidBST(self, root, min, max):
    if root is None or root.val is None:
        return True
    return root.val < max \
        and root.val > min \
        and self._isValidBST(root.left, min, root.val) \
        and self._isValidBST(root.right, root.val, max)