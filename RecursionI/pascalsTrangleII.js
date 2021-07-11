const getRow = (rowIndex) => {
    let prev = []
    for (let i = 0; i <= rowIndex; i++) {
        const current = []
        for (let j = 0; j <= i; j++) {
            if (prev[j] && prev[j - 1]) {
                current.push(prev[j] + prev[j - 1])
            } else {
                current.push(1)
            }
        }
        prev = current
    }
    return prev
}