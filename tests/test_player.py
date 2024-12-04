# test/test_player.py
import unittest
from unittest.mock import patch
from source.player import pon  # pon() 関数が定義されている場所をインポート

class TestPonFunction(unittest.TestCase):
    def test_pon_valid_input(self):
        # ユーザー入力をモックして、'1'（グー）を選択させる
        with patch('builtins.input', return_value='1'):
            result = pon()
            self.assertEqual(result, "グー")

        # ユーザー入力をモックして、'2'（チョキ）を選択させる
        with patch('builtins.input', return_value='2'):
            result = pon()
            self.assertEqual(result, "チョキ")

        # ユーザー入力をモックして、'3'（パー）を選択させる
        with patch('builtins.input', return_value='3'):
            result = pon()
            self.assertEqual(result, "パー")

    def test_pon_invalid_input(self):
        # 無効な入力があった場合、再度入力を求めるか確認する
        with patch('builtins.input', side_effect=['4', '2']):  # 最初に無効な入力、次に有効な入力
            result = pon()
            self.assertEqual(result, "チョキ")

if __name__ == '__main__':
    unittest.main()