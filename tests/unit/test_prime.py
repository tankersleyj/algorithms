# MIT (c) jtankersley 2019-05-19
import unittest
from src import prime
from src import timer


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        value = 997
        print(f"test_is_prime({value})")
        actual, divisor = timer.run_timed_result(prime.is_prime, 997)
        expected = True
        self.assertEqual(actual, expected, f'is_prime({value}), divisor={divisor}')

    def test_get_primes(self):
        start = 990
        end = 999
        print(f"test_get_primes({start}, {end})")
        actual = timer.run_timed_result(prime.get_primes, start, end)
        expected = [991,997]
        self.assertEqual(actual, expected, f'get_primes({start}, {end})')

    def test_list_primes(self):
        start = 990
        end = 999
        verbose = False
        print(f"test_list_primes({start}, {end}, {verbose})")
        actual = timer.run_timed_result(prime.list_primes, start, end, verbose)
        expected = 2
        self.assertEqual(actual, expected, f'list_primes({start}, {end})')

    def test_isPrime(self):
        value = 997
        print(f"test_isPrime({value})")
        p = prime.Prime()
        actual = timer.run_timed_result(p.isPrime, value)
        expected = True
        self.assertEqual(actual, expected, f'isPrime({value})')

    def test_getPrimes(self):
        start = 990
        end = 999
        p = prime.Prime()
        print(f"test_getPrimes({start}, {end})")
        actual = timer.run_timed_result(p.getPrimes, start, end)
        expected = [991,997]
        self.assertEqual(actual, expected, f'getPrimes({start}, {end})')

    def test_computePrimes(self):
        start = 990
        end = 999
        logPrimes = True
        logNonPrimes = False
        print(f"test_computePrimes({start}, {end}, {logPrimes}, {logNonPrimes})")
        p = prime.Prime()
        actual = timer.run_timed_result(p.computePrimes, end, logPrimes, logNonPrimes)
        expected = 1009
        self.assertEqual(actual, expected, f'listPrimes({start}, {end})')

    def test_listPrimes(self):
        start = 990
        end = 999
        print(f"test_listPrimes({start}, {end})")
        p = prime.Prime()
        actual = timer.run_timed_result(p.listPrimes, start, end)
        expected = 2
        self.assertEqual(actual, expected, f'listPrimes({start}, {end})')
