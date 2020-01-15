// MIT (c) jtankersley 2020-01-12, compare values and arrays
function minFactor(value) {
    var result = value, maxFactor = Math.floor(Math.sqrt(value)) + 1;
    if (value > 3) {
        for (var i = 2; i <= maxFactor; i++) {
            if (value % i === 0) {
                result = i;
                break;
            }
        }
    }
    return result; // value or min factor > 1
}
function getPrimes(start, end) {
    var primeArray = [];
    for (var i = start; i <= end; i++) {
        if (i !== 2 && i === minFactor(i)) {
            primeArray.push(i);
        }
    }
    return primeArray;
}
// Test (Code Runner: ctrl+option+n)
(function test() {
    console.log(minFactor(1)); // expect 1
    console.log(minFactor(2)); // expect 2
    console.log(minFactor(4)); // expect 2
    console.log(minFactor(7)); // expect 7
    console.log(minFactor(49)); // expect 7
    console.log(getPrimes(1, 10)); // expect 1,3,5,7
    console.log(getPrimes(11, 50)); // expect 11,13,17,19,23,29,31,37,41,43,47
    console.log(getPrimes(53, 97)); // expect 53,59,61,67,71,73,79,83,89,97
})();
