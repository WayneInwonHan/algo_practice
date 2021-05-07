def reverse(self, x):
    arr = []
    f = False
    if x < 0:
        x *= -1
        f = True
    while True:
        arr.append(x % 10)
        x /= 10
        if x == 0:
            break
    result = 0
    for i in arr:
        result = i + 10 * result
    if f:
        result *= -1
    return result