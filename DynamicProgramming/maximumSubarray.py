def maxSubArray(self, A):
    global_max, local_max = float("-inf"), 0
    for x in A:
        local_max = max(0, local_max + x)
        global_max = max(global_max, local_max)
    return global_max