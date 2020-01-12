// refactored from: https://www.guru99.com/quicksort-in-javascript.html

function swap(items, leftIndex, rightIndex){
    var temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
}

function partition(items, left, right) {
    var pivot = items[Math.floor((right + left) / 2)], // middle element
        i = left, // left pointer
        j = right; // right pointer
    while (i <= j) {
        while (items[i] < pivot) {i++}
        while (items[j] > pivot) {j--}
        if (i <= j) {swap(items, i++, j--)} // [de]increment i and j after call to swap
    }
    return i;
}

function quickSort(items, left, right) {
    var index;
    if (items.length > 1) {
        index = partition(items, left, right); // index returned from partition
        if (left < index - 1) {quickSort(items, left, index - 1)} // more elements on the left side of the pivot (+1)
        if (right > index) {quickSort(items, index, right)} // more elements on the right side of the pivot
    }
    return items;
}

// first call to quick sort (highlightCode > rightClick > Run Code)
(function test_quickSort() {
    var items = [5,3,7,6,2,9,1,-4,-9,0,8,-3];
    var sortedArray = quickSort(items, 0, items.length - 1);
    console.log(sortedArray); // prints [ -9, -4, -3, 0, 1, 2, 3, 5, 6, 7, 8, 9 ]
})()
