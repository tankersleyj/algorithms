// MIT (c) jtankersley 2020-01-12, Quick Sort (log n)
// refactored by J.Tankersley from: https://www.guru99.com/quicksort-in-javascript.html

function quickSort(items) { // array
    function _arraySwap(items, left, right){ // array, left index, right index
        var temp = items[left];
        items[left] = items[right];
        items[right] = temp;
    }
    function _partition(items, left, right) { // array, left index, right index
        var pivot = items[Math.floor((left + right) / 2)], // middle value
            i = left, // left pointer
            j = right; // right pointer
        while (i < j) {
            while (items[i] < pivot) {i++}
            while (items[j] > pivot) {j--}
            if (i < j) {_arraySwap(items, i++, j--)} // [de]increment pointers after call to swap
        }
        return i; // middle index
    }
    function _recur(items, left, right) { // array, left index, right index
        var middle;
        if (items.length > 1) {
            middle = _partition(items, left, right); // index returned from partition
            if (left < middle - 1) {_partition(items, left, middle - 1)} // more elements on the left side of the pivot (non-inclusive)
            if (right > middle) {_partition(items, middle, right)} // more elements on the right side of the pivot (inclusive)
        }
        return items;
    }
    return _recur(items, 0, items.length - 1);
}

// Test (Code Runner: ctrl+option+n)
(function test_quickSort() {
    var items = [5,3,7,-2,6,2,9,1,-4,-9,0,8,-3];
    console.log(quickSort(items)); // expect: [ -9, -4, -3, -2, 0, 1, 2, 3, 5, 6, 7, 8, 9 ]
    console.log(items); // expect: [ -9, -4, -3, -2, 0, 1, 2, 3, 5, 6, 7, 8, 9 ]
    console.log(quickSort([1])); // expect: [ 1 ]
    console.log(quickSort([1,2])); // expect: [ 1, 2 ]
    console.log(quickSort([5,3])); // expect: [ 3, 5 ]
    console.log(quickSort([2,1,3])); // expect: [ 1, 2, 3 ]
})()
