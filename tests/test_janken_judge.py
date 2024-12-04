import unittest
from source.janken_judge import judge  # judge() 関数が定義されている場所をインポート

class TestJudgeFunction(unittest.TestCase):
    def test_draw(self):
        # あいこのテスト: プレイヤーとコンピュータが同じ手を出した場合
        self.assertEqual(judge("グー", "グー"), "あいこです！")
        self.assertEqual(judge("チョキ", "チョキ"), "あいこです！")
        self.assertEqual(judge("パー", "パー"), "あいこです！")

    def test_player_win(self):
        # プレイヤーが勝つ場合のテスト
        self.assertEqual(judge("グー", "チョキ"), "あなたの勝ちです！")
        self.assertEqual(judge("チョキ", "パー"), "あなたの勝ちです！")
        self.assertEqual(judge("パー", "グー"), "あなたの勝ちです！")

    def test_computer_win(self):
        # コンピュータが勝つ場合のテスト
        self.assertEqual(judge("グー", "パー"), "コンピューターの勝ちです！")
        self.assertEqual(judge("チョキ", "グー"), "コンピューターの勝ちです！")
        self.assertEqual(judge("パー", "チョキ"), "コンピューターの勝ちです！")

if __name__ == '__main__':
    unittest.main()
