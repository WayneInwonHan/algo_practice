const triangleNumber = (nums = []) => {
    nums.sort((a, b) => a - b)
    let k = 2
    let count = 0
    for (let i = 0; i < nums.length - 2; i++) {
      for (let j = i + 1; j < nums.length - 1; j++) {
        k = j + 1
        while (nums[k] < nums[i] + nums[j]) {
          k += 1
        }
        count += k - j - 1
      }
    }
    return count
}