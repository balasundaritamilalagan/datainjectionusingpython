import unittest
def calculate_rectangle_area(width,height):
    return width*height

class TestRectangleArea(unittest.TestCase):
    pass

class TestRectangleArea(unittest.TestCase):
    def test_area_calculation(self):
        self.assertEqual(calculate_rectangle_area(3,4),12)
        self.assertEqual(calculate_rectangle_area(0,10),0)
        self.assertEqual(calculate_rectangle_area(5,5),25)
        self.assertEqual(calculate_rectangle_area(8,2),16)
#8*2 =16 ok va thappa kudutha test cass fail agudhu paru crt ah kudutha tha run agum purinjidha purila

if __name__=='--main--':
    if __name__ == '__main__':
        unittest.main()




