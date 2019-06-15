#  MIT (c) jtankersley 2019-05-18
from src import timer
import math


def is_prime(value):
    # return Boolean, Divisor
    if value == 1:
        return False, value
    if value % 2 == 0:
        return False, 2
    for i in range(3, round(math.sqrt(value)) + 1, 2):
        if value % i == 0:
            return False, i
    return True, value


def get_primes(start, end):
    # return prime list
    primes = []
    for i in range(start, end + 1):
        prime, divisor = is_prime(i)
        if prime:
            primes.append(i)
    return primes


def list_primes(start, end, verbose=False):
    # print primes (and optionally non-primes with divisor)
    count_primes = 0
    print(f"list primes: {start} through {end}")
    for i in range(start, end + 1):
        prime, divisor = is_prime(i)
        if prime:
            count_primes += 1
            print(f"{i} is prime")
        elif verbose:
            print(f"{i} divisible by {divisor}")
    return count_primes


class Prime():

    def __init__(self):
       self.primes = [3,5,7,11,13,17,19,23]

    def _computeNext(self, logPrimes=False, logNonPrimes=False):
        index = 0
        max_index = len(self.primes) - 1
        value = self.primes[max_index]
        is_prime = False
        while is_prime == False:
            value += 2  # primes are always odd (odd + 2 = odd)
            value_sqrt = round(math.sqrt(value))
            is_prime = True
            for index in range(0, max_index):
                divisor = self.primes[index]
                if divisor > value_sqrt:
                    break # is prime
                elif value % divisor == 0:
                    is_prime = False
                    break  # not prime
            if is_prime == True:
                self.primes.append(value)
                if logPrimes:
                    print(f"{value} is prime")
                return value  
            else:
                if logNonPrimes:
                    print(f"{value} divisible by {divisor}")

    def _getMid(self, start, end):
        return start + (end - start) // 2

    def _getIndexLte(self, value):
        def _getIndexLte(value, min_index, max_index):
            index = self._getMid(min_index, max_index)
            if index > min_index and index < max_index:
                mid_value = self.primes[index]
                if value < mid_value:
                    return _getIndexLte(value, min_index, index)
                else:
                    return _getIndexLte(value, index, max_index)
            else:
                return min_index
        return _getIndexLte(value, 0, len(self.primes) - 1)
        
    def _getIndexGte(self, value):
        def _getIndexGte(value, min_index, max_index):
            index = self._getMid(min_index, max_index)
            if index > min_index and index < max_index:
                mid_value = self.primes[index]
                if value < mid_value:
                    return _getIndexGte(value, min_index, index)
                else:
                    return _getIndexGte(value, index, max_index)
            else:
                return max_index
        return _getIndexGte(value, 0, len(self.primes) - 1)

    def computePrimes(self, max_value, logPrimes=False, logNonPrimes=False):
        # fill prime list
        max_prime = self.primes[len(self.primes) - 1]
        while max_prime < max_value:
            self._computeNext(logPrimes, logNonPrimes)
            max_index = len(self.primes) - 1
            max_prime = self.primes[max_index]
        return max_prime

    def isPrime(self, value):
        # return prime
        self.computePrimes(value)
        return value in self.primes

    def getPrimes(self, start, end):
        # return prime list
        self.computePrimes(end)
        start_index = self._getIndexGte(start)
        end_index = self._getIndexLte(end)
        print(f"getPrimes: prime[{start_index}]={self.primes[start_index]}({start}) through prime[{end_index}]={self.primes[end_index]}({end})")
        return self.primes[start_index:end_index]

    def listPrimes(self, start, end):
        # print prime list
        self.computePrimes(end)
        start_index = self._getIndexGte(start)
        end_index = self._getIndexLte(end)
        count_primes = 0
        print(f"listPrimes: prime[{start_index}]={self.primes[start_index]}({start}) through prime[{end_index}]={self.primes[end_index]}({end})")
        for i in range(start_index, end_index + 1):
            count_primes += 1
            print(f"{self.primes[i]} is prime")
        return count_primes
