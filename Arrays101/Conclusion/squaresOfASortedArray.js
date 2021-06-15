const sortedSquares = function (A) {
    const result = []
    let left = 0
    let right = A.length - 1
    while (left <= right) {
        const leftSquare = A[left] * A[left]
        const rightSquare = A[right] * A[right]
        if (leftSquare < rightSquare) {
            result.push(rightSquare)
            right -= 1
        } else {
            result.push(leftSquare)
            left += 1
        }
    }
    return result.reverse()
}