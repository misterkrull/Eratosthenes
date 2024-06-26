import unittest

from main import sieve_of_eratosthenes


class EratostheneTest(unittest.TestCase):
    def test_10(self):
        res, p_max = sieve_of_eratosthenes(10)
        self.assertListEqual([2, 3, 5, 7], res)
        self.assertEqual(3, p_max)
        
    def test_100(self):
        res, p_max = sieve_of_eratosthenes(100)
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], res)
        self.assertEqual(7, p_max)
        
    def test_1000(self):
        res, p_max = sieve_of_eratosthenes(1000)
        self.assertEqual(168, len(res))
        self.assertEqual(997, res[-1])
        self.assertEqual(31, p_max)
        
    def test_2(self):
        res, p_max = sieve_of_eratosthenes(2)
        self.assertListEqual([2], res)
        self.assertEqual(0, p_max)
        
    def test_1(self):
        res, p_max = sieve_of_eratosthenes(1)
        self.assertListEqual([], res)
        self.assertEqual(0, p_max)
    
    def test_negative_1(self):
        res, p_max = sieve_of_eratosthenes(-1)
        self.assertListEqual([], res)
        self.assertEqual(0, p_max)
    
    def test_negative_42(self):
        res, p_max = sieve_of_eratosthenes(-42)
        self.assertListEqual([], res)
        self.assertEqual(0, p_max)
    
    