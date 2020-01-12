// Quick Sort (log n)
// refactored by J.Tankersley from: https://www.guru99.com/quicksort-in-javascript.html

function qs_arraySwap(items, leftIndex, rightIndex){
    var temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
}

function qs_partition(items, left, right) {
    var pivot = items[Math.floor((left + right) / 2)], // middle element
        i = left, // left pointer
        j = right; // right pointer
    while (i < j) {
        while (items[i] < pivot) {i++}
        while (items[j] > pivot) {j--}
        if (i < j) {qs_arraySwap(items, i++, j--)} // [de]increment i and j after call to swap
    }
    return i;
}

function qs_recur(items, left, right) {
    var index;
    if (items.length > 1) {
        index = qs_partition(items, left, right); // index returned from partition
        if (left < index - 1) {qs_partition(items, left, index - 1)} // more elements on the left side of the pivot (non-inclusive)
        if (right > index) {qs_partition(items, index, right)} // more elements on the right side of the pivot (inclusive)
    }
    return items;
}

function quickSort(items) {
    return qs_recur(items, 0, items.length - 1);
}

// Test (Code Runner: cmd+a > right+click > Run Code | mac: ctrl+option+n)
(function test_quickSort() {
    var items = [5,3,7,-2,6,2,9,1,-4,-9,0,8,-3];
    console.log(quickSort(items)); // expect: [ -9, -4, -3, -2, 0, 1, 2, 3, 5, 6, 7, 8, 9 ]
    console.log(items); // expect: [ -9, -4, -3, -2, 0, 1, 2, 3, 5, 6, 7, 8, 9 ]
    console.log(quickSort([1])); // expect: [ 1 ]
    console.log(quickSort([1,2])); // expect: [ 1, 2 ]
    console.log(quickSort([5,3])); // expect: [ 3, 5 ]
    console.log(quickSort([2,1,3])); // expect: [ 1, 2, 3 ]
})()
