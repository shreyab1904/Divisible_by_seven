import unittest

def add(x,y):
    return x+y

class MyApp2(unittest.TestCase):
    def test_case1(self):
        a=10
        b=22
        c=add(a,b)
        self.assertEqual(a+b,c)
    def test_case2(self):
        a=12.5
        b=19.2
        c=add(a,b)
        self.assertEqual(a+b,c)

if __name__=="__main__":
    unittest.main()