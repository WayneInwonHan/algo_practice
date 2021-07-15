class Solution(object):
    def generateTrees(self, n):
        if n<1:
            return []
        cache = {}
        def generate(first, last):
            if first>last:
                return [None]
            if (first, last) in cache:
                return cache[first, last]
            trees = []
            for i in range(first, last+1):
                for left in generate(first, i-1):
                    for right in generate(i+1, last):
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        trees.append(node)
            cache[first, last] = trees
            return trees
        return generate(1, n)