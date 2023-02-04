import unittest

def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):
    def test(self):
        a = 10
        b = 20

        result = sum(a, b)

        #self.assertEqual(result, 31)
        self.assertEqual(result, a + b)

if __name__ == "__main__":
    unittest.main()
