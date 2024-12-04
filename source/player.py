def pon():
    while (True):
        hand = int(input('1.グー 2.チョキ 3.パー \n あなたの手を選択してください。>'))
        if hand == 1:
            hand = "グー"
            return hand
        elif hand == 2:
            hand = "チョキ"
            return hand
        elif hand == 3:
            hand = "パー"
            return hand
        else:
            print("無効な入力です。\n1,2,3の中から再度入力してください。")


