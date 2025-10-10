import unittest
from src.main import ice_skating_price

class TestPhuC2(unittest.TestCase):
    def test_T3_non_member(self):
        self.assertEqual(ice_skating_price("T3", False), 170000)

    def test_T5_member(self):
        self.assertEqual(ice_skating_price("T5", True), 136000)

    def test_T7_non_member(self):
        self.assertEqual(ice_skating_price("T7", False), 220000)

    def test_CN_member(self):
        self.assertEqual(ice_skating_price("CN", True), 176000)

    def test_T0_invalid(self):
        self.assertEqual(ice_skating_price("T0", False), "Invalid")

    def test_T1_invalid(self):
        self.assertEqual(ice_skating_price("T1", True), "Invalid")

if __name__ == '__main__':
    unittest.main()
