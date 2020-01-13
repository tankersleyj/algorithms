// MIT (c) jtankersley 2020-01-12, fibonacci searies

function getFibRecur(n) { // reurn value at index n of [0,1,1,2,3,5,8,13,21,34,...]
    if (n<1) return 0
    else if (n==1) return 1
    else return getFibRecur(n-1) + getFibRecur(n-2);
}

function getFibNumber(n) { // reurn value at index n of [0,1,1,2,3,5,8,13,21,34,...]
    let result, a=0, b=1, c=0;
    for (let i=0; i<=n; i++) {
        result = a;
        c = a+b;
        a = b;
        b = c;
    }
    return result;
}

function getFibNumbers(n) { // reurn values inclusive of index n of [0,1,1,2,3,5,8,13,21,34,...]
    let numbers=[], a=0, b=1, c=0;
    for (let i=0; i<=n; i++) {
        numbers.push(a);
        c = a+b;
        a = b;
        b = c;
    }
    return numbers;
}

(function test_getFibN() {
    console.log(getFibRecur(0)); // expect 0
    console.log(getFibRecur(1)); // expect 1
    console.log(getFibRecur(2)); // expect 1
    console.log(getFibRecur(3)); // expect 2
    console.log(getFibRecur(4)); // expect 3
    console.log(getFibRecur(5)); // expect 5
    console.log(getFibNumber(0)); // expect 0
    console.log(getFibNumber(1)); // expect 1
    console.log(getFibNumber(2)); // expect 1
    console.log(getFibNumber(3)); // expect 2
    console.log(getFibNumber(4)); // expect 3
    console.log(getFibNumber(5)); // expect 5
    console.log(getFibNumbers(0)); // expect [0]
    console.log(getFibNumbers(1)); // expect [0,1]
    console.log(getFibNumbers(8)); // expect [0,1,1,2,3,4,8,13,21]
})()