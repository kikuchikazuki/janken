import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))
import unittest
from unittest.mock import patch
import io
import source.player as p
import source.computer as c
import source.janken_judge as jj
import source.janken as jm

class TestJankenMain(unittest.TestCase):
    @patch('player.pon')
    @patch('computer.pon')
    @patch('janken_judge.judge')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_janken_main(self, mock_stdout, mock_judge, mock_computer_pon, mock_player_pon):
        # モックの設定
        mock_player_pon.side_effect = ['グー', 'チョキ', 'パー']  # プレイヤーの手
        mock_computer_pon.side_effect = ['チョキ', 'パー', 'グー']  # コンピューターの手
        mock_judge.side_effect = ['あなたの勝ちです！', 'コンピューターの勝ちです！', 'あいこです！']  # 審判結果

        # janken_main を実行
        jm.janken_main()

        # 出力の確認
        output = mock_stdout.getvalue()

        # 結果を確認
        self.assertIn("-----ラウンド1-----", output)
        self.assertIn("あなたの手はグーです。", output)
        self.assertIn("コンピューターの手はチョキです。", output)
        self.assertIn("あなたの勝ちです！", output)
        
        self.assertIn("-----ラウンド2-----", output)
        self.assertIn("あなたの手はチョキです。", output)
        self.assertIn("コンピューターの手はパーです。", output)
        self.assertIn("コンピューターの勝ちです！", output)

        self.assertIn("-----ラウンド3-----", output)
        self.assertIn("あなたの手はパーです。", output)
        self.assertIn("コンピューターの手はグーです。", output)
        self.assertIn("あいこです！", output)

        self.assertIn("【最終結果】", output)
        self.assertIn("あなた：1勝", output)
        self.assertIn("コンピューター：1勝", output)
        self.assertIn("コンピューターの総合勝利です！", output)

if __name__ == '__main__':
    unittest.main()