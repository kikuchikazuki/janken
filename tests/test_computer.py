import unittest
from unittest.mock import patch
from source.computer import pon  # pon() 関数が定義されている場所をインポート

class TestPonFunction(unittest.TestCase):
    def test_pon_computer_choice(self):
        # random.uniform の戻り値をモックして、それぞれの選択肢をテストする
        with patch('random.uniform', return_value=1.5):  # "グー" の選択を模倣
            result = pon()
            self.assertEqual(result, "グー")

        with patch('random.uniform', return_value=2.5):  # "チョキ" の選択を模倣
            result = pon()
            self.assertEqual(result, "チョキ")

        with patch('random.uniform', return_value=3.5):  # "パー" の選択を模倣
            result = pon()
            self.assertEqual(result, "パー")

if __name__ == '__main__':
    unittest.main()
        
        