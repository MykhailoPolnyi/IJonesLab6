import unittest
from ijones.ijones import ijones
from ijones.ijones_reader import read_plate_file


class TestIJones(unittest.TestCase):
    def test_1_plate(self):
        self.assertEqual(ijones(1, 1, "a"), 1)

    def test_wrong_input(self):
        self.assertRaises(IndexError, ijones, 2, 3, ("an", "io"))
        self.assertRaises(IndexError, ijones, 3, 2, ("oi", "bo"))

    def test_input_1(self):
        input_file_params = read_plate_file("../ijones.in1.txt")
        self.assertEqual(ijones(*input_file_params), 5)

    def test_input_2(self):
        input_file_params = read_plate_file("../ijones.in2.txt")
        self.assertEqual(ijones(*input_file_params), 2)

    def test_input_3(self):
        input_file_params = read_plate_file("../ijones.in3.txt")
        self.assertEqual(ijones(*input_file_params), 201684)


if __name__ == '__main__':
    unittest.main()
