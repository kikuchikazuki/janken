import random as r
def pon():
    computer = (r.uniform(1,4))
    computer = int(computer)
    
    if computer == 1:
        c_hand = "グー"
        return c_hand
    elif computer == 2:
        c_hand = "チョキ"
        return c_hand
    elif computer == 3:
        c_hand = "パー"
        return c_hand
