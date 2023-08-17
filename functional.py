import unittest

def calculate_rectangle_area(length,width):
    return length*width;

class  TestRectangleAreaCalculation(unittest.TestCase):

    def test_positive_case(self):
        self.assertEqual(calculate_rectangle_area(5,10),50)

    def test_zero_values(self):
        self.assertEqual(calculate_rectangle_area(0,10),0)
        self.assertEqual(calculate_rectangle_area(5,0),0)

    def test_negative_values(self):
        self.assertEqual(calculate_rectangle_area(-5,10),-50)
        self.assertEqual(calculate_rectangle_area(5,-10),-50)

if __name__=='__main__':
    unittest.main()
