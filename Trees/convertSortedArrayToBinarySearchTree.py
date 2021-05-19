def sortedArrayToBST(self, num):
    return self.sortedArrayToBSTRecu(num, 0, len(num))

@staticmethod
def perfect_tree_pivot(n):
    x = 1
    x = 1 << (n.bit_length() - 1)

    if x // 2 - 1 <= (n - x):
        return x - 1
    else:
        return n - x // 2

def sortedArrayToBSTRecu(self, num, start, end):
    if start == end:
        return None
    mid = start + self.perfect_tree_pivot(end - start)
    node = TreeNode(num[mid])
    node.left = self.sortedArrayToBSTRecu(num, start, mid)
    node.right = self.sortedArrayToBSTRecu(num, mid + 1, end)
    return node