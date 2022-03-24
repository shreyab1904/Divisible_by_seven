import unittest

def checkDivisible7(x):
    if x%7==0:
        return True
    else:
        return False

class checkDivisible(unittest.TestCase):
    def test_case_divisible(self):
        x=14
        result=checkDivisible7(x)
        self.assertTrue(result)
    def test_case_divisible1(self):
        x=9;
        result=checkDivisible7(x)
        self.assertFalse(result)


if __name__=="__main__":
    unittest.main()