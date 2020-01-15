// MIT (c) jtankersley 2020-01-12, Quick Sort (log n) and Bubble Sort (n^2)
// reference: https://www.guru99.com/quicksort-in-javascript.html

function swapItemValues(items:number[], i:number, j:number):void {
    let temp = items[i];
    items[i] = items[j];
    items[j] = temp;
}

function bubbleSort(items:number[]):number[] { // small list, n^2 efficiency
    for (let i=0; i<items.length; i++) {
        for (let j=i; j<items.length; j++) {
            if (items[i] > items[j]) {swapItemValues(items, i, j)}
        }
    }
    return items
}

function quickSort(items:number[]):number[] { // large list, log n efficiency
    function _partition(items, left, right) {
        let midVal=items[Math.floor((left + right) / 2)], i=left, j=right;
        while (i < j) {
            while (items[i] < midVal) {i++}
            while (items[j] > midVal) {j--}
            if (i < j) {swapItemValues(items, i++, j--)}
        }
        return i;
    }
    function _recur(items:number[], left:number, right:number, priorState:any=undefined):number[] {
        let middle, newState;
        if (items.length > 1) {
            middle = _partition(items, left, right);
            newState = {li:left, mi:middle, ri:right, lv:items[left], mv:items[middle], rv:items[right]};
            if (JSON.stringify(newState) != JSON.stringify(priorState)) {
                if (left < middle) {_recur(items, left, middle, newState)}
                if (right > middle + 1) {_recur(items, middle + 1, right, newState)}
            }
        }
        return items;
    }
    return _recur(items, 0, items.length - 1);
}

// Test (Code Runner: ctrl+option+n)
(function testSort() {
    let orderedItems = [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32];
    let unOrderedItems = [10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8];
    let duplicateItems = [8,6,4,2,4,6,8,3,5,5,5,7,9,2,4,8];
    let negativeItems = [5,3,7,-2,6,2,9,1,-4,-9,0,8,-3];
    // bubble sort
    console.log(bubbleSort([1])); // expect: [1]
    console.log(bubbleSort([1,2])); // expect: [1,2]
    console.log(bubbleSort([5,3])); // expect: [3,5]
    console.log(bubbleSort([2,1,3])); // expect: [1,2,3]
    console.log(bubbleSort(orderedItems)); // expect: [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
    console.log(bubbleSort(unOrderedItems)); // expect: [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
    console.log(bubbleSort(duplicateItems)); // expect: [1,2,2,3,4,4,4,5,5,5,6,6,7,8,8,8,9]
    console.log(bubbleSort(negativeItems)); // expect: [-9,-4,-3,-2,0,1,2,3,5,6,7,8,9]
    // quick sort
    console.log(quickSort([1])); // expect: [1]
    console.log(quickSort([1,2])); // expect: [1,2]
    console.log(quickSort([5,3])); // expect: [3,5]
    console.log(quickSort([2,1,3])); // expect: [1,2,3]
    console.log(quickSort(orderedItems)); // expect: [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
    console.log(quickSort(unOrderedItems)); // expect: [1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32]
    console.log(quickSort(duplicateItems)); // expect: [1,2,2,3,4,4,4,5,5,5,6,6,7,8,8,8,9]
    console.log(quickSort(negativeItems)); // expect: [-9,-4,-3,-2,0,1,2,3,5,6,7,8,9]
})()
