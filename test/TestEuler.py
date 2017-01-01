import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")

import Euler
import unittest

class Fast(unittest.TestCase):

    def setUp(self):
        pass

    def testPrimes(self):
        self.assertTrue(all(Euler.is_prime(i) for i in [3,5,7,11]))
        self.assertFalse(all(not Euler.is_prime(i) for i in [0,1,2]))

    def testPrimefactors(self):
        r = Euler.prime_factors(12)
        r.sort()
        self.assertEqual(r,[2,2,3])
        
        r = Euler.prime_factors(13)
        r.sort()
        self.assertEqual(r,[13])
        
        r = Euler.prime_factors(3000)
        r.sort()
        self.assertEqual(r, [2,2,2,3,5,5,5])

    def testFindDivisor(self):
        r = Euler.find_divisor(12)
        self.assertEqual(0, 12%r)

    def testDivCount(self):
        self.assertEqual(Euler.div_count(13),2)
        self.assertEqual(Euler.div_count(14),4)
        self.assertEqual(Euler.div_count(18),6)
        self.assertEqual(Euler.div_count(1100),18)


    def testDivSum(self):
        self.assertEqual(Euler.div_sum(13), 1)
        self.assertEqual(Euler.div_sum(14), 10)
        self.assertEqual(Euler.div_sum(18), 21)
        self.assertEqual(Euler.div_sum(1100), 1504)
        self.assertEqual(Euler.div_sum(20161), 1)

