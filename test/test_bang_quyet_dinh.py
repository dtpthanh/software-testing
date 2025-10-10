import unittest
from src.main import ice_skating_price

class TestBangQuyetDinh(unittest.TestCase):
    
    def test_case_1_invalid_day_member_true(self):
        self.assertEqual(ice_skating_price("T0", True), "Invalid")

    def test_case_2_invalid_day_member_false(self):
        self.assertEqual(ice_skating_price("T1", False), "Invalid")

    def test_case_3_weekday_member_true(self):
        self.assertEqual(ice_skating_price("T5", True), 136000)

    def test_case_4_weekday_member_false(self):
        self.assertEqual(ice_skating_price("T5", False), 170000)

    def test_case_5_weekend_member_true(self):
        self.assertEqual(ice_skating_price("T7", True), 176000)

    def test_case_6_weekend_member_false(self):
        self.assertEqual(ice_skating_price("CN", False), 220000)


if __name__ == "__main__":
    unittest.main()
