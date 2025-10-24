import unittest
from src.main import ice_skating_price   

class TestAllUses(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(ice_skating_price("T1", True), "Invalid")

    def test_case_02(self):
        self.assertEqual(ice_skating_price("T7", False), 220000)

    def test_case_03(self):
        self.assertEqual(ice_skating_price("T7", True), 176000)

    def test_case_04(self):
        self.assertEqual(ice_skating_price("T3", True), 136000)

    def test_case_05(self):
        self.assertEqual(ice_skating_price("T7", True), 176000)

    def test_case_06(self):
        self.assertEqual(ice_skating_price("T3", False), 170000)

    def test_case_07(self):
        self.assertEqual(ice_skating_price("T7", False), 220000)

    def test_case_08(self):
        self.assertEqual(ice_skating_price("T3", True), 136000)

if __name__ == "__main__":
    unittest.main()
