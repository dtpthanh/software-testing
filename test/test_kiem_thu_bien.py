import unittest
from src.main import ice_skating_price

class TestKiemThuBien(unittest.TestCase):

    def test_T2_member_true(self):
        self.assertEqual(ice_skating_price("T2", True), 136000)  

    def test_T2_member_false(self):
        self.assertEqual(ice_skating_price("T2", False), 170000)

    def test_T3_member_true(self):
        self.assertEqual(ice_skating_price("T3", True), 136000)

    def test_T3_member_false(self):
        self.assertEqual(ice_skating_price("T3", False), 170000)

    def test_T5_member_true(self):
        self.assertEqual(ice_skating_price("T5", True), 136000)

    def test_T5_member_false(self):
        self.assertEqual(ice_skating_price("T5", False), 170000)

    # --- Ranh giới cuối tuần (T7, CN) ---
    def test_T7_member_true(self):
        self.assertEqual(ice_skating_price("T7", True), 176000)  

    def test_T7_member_false(self):
        self.assertEqual(ice_skating_price("T7", False), 220000)

    def test_CN_member_true(self):
        self.assertEqual(ice_skating_price("CN", True), 176000)

    def test_CN_member_false(self):
        self.assertEqual(ice_skating_price("CN", False), 220000)


if __name__ == "__main__":
    unittest.main()
