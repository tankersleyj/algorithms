// MIT (c) jtankersley 2020-01-12, compare values and arrays
// reference: // https://javascript.info/comparison

function compareValues(value1, value2) {
    if (value1 > value2) return 1;
    else if (value1 < value2) return -1;
    else return 0;
}

// compare arrays from left to right (a1>a2=1, a1<a2=-1, else 0)
function compareArrays(a1, a2) {
    let result=0, maxIndex=Math.max(a1.length, a2.length);
    for (let i=0; i<maxIndex; i++) {
        result = compareValues(a1[i], a2[i]); // cast out of bounds to undefined
        if (result != 0) break;
    }
    return result;
}

function compareValuesAsNumber(value1, value2) {
    let number1 = (value1) ? Number(value1) : 0;
    let number2 = (value2) ? Number(value2) : 0;
    return compareValues(number1, number2);
}

function compareValuesAsString(value1, value2) {
    let string1 = (value1) ? value1.toString() : "";
    let string2 = (value2) ? value2.toString() : "";
    return compareValues(string1, string2);
}

// compare arrays from left to right (a1>a2=1, a1<a2=-1, else 0)
function compareArraysAs(a1, a2, method) {
    let result=0, compareFunc, maxIndex=Math.max(a1.length, a2.length);
    if (typeof method === "function") {compareFunc=method}  // user defined
    else if (method==="Number") {compareFunc=compareValuesAsNumber} // cast Number
    else if (method==="String") {compareFunc=compareValuesAsString} // cast String
    else {compareFunc=compareValues}; // no explicit cast
    for (let i=0; i<maxIndex; i++) {
        result = compareFunc(a1[i], a2[i]); // cast out of bounds to undefined
        if (result != 0) break;
    }
    return result;
}

// Test (Code Runner: ctrl+option+n)
(function test() {
    // default
    console.log(compareArrays([1,2,"3"], [1,2,"10"])) // expect 1 (string compare)
    console.log(compareArrays([1,2,3], [1,2])) // expect 0 (ignore undefined)
    console.log(compareArrays([1,2,3], [1,2,"10"])) // expect -1 (number compare)
    // Number
    console.log(compareArraysAs([1,2,"10"], [1,2,"3"], "Number")) // expect 1 (number compare)
    console.log(compareArraysAs([1,2,0], [1,2,"000"], "Number")) // expect 0 (number compare)
    console.log(compareArraysAs([1,2], [1,2,3], "Number")) // expect -1 (undefined as 0)
    // string
    console.log(compareArraysAs([1,2,"3"], [1,2,"10"], "String")) // expect -1 (string compare)
    console.log(compareArraysAs([1,2,"3"], [1,2,3], "String")) // expect 0 (string compare)
    console.log(compareArraysAs([1,2], [1,2,"0"], "String")) // expect 1 (undefined as "")
    // custom
    console.log(compareArraysAs([1,2,"3"], [1,2,"10"], compareValues)) // expect 1 (string compare)
    console.log(compareArraysAs([1,2,0], [1,2,"000"], compareValuesAsNumber)) // expect 0 (number compare)
    console.log(compareArraysAs([1,2], [1,2,"0"], compareValuesAsString)) // expect 1 (undefined as "")
})()