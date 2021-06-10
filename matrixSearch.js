
givenArray = [
    [0, 0, 1, 2],
    [0, 0, 3, 3],
    [1, 1, 2, 3],
    [3, 3, 4, 4]
]

item = [
    [1, 2],
    [3, 4]
]

function isItemInArray(array, item) {
    for (var i = 0; i < array.length; i++) {
        for (var j = 0; j < array.length; j++) {
            if (array[i][j] == item[0][0] 
                && array[i][j+1] == item[0][1]
                && array[i+1][j] == item[1][0]
                && array[i+1][j+1] == item[1][1]) {
                
                console.log([i,j])
                return true;
            }
        } 
    }
    console.log([-1,-1])
    return false;
}

console.log(isItemInArray(givenArray, item));