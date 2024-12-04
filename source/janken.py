import player as p
import computer as c
import janken_judge as jj

def janken_main():
    p_cnt = 0
    c_cnt = 0
    for i in range(1,4):
        print(f'-----ラウンド{int(i)}-----')
        you = p.pon()
        print(f'あなたの手は{you}です。')
        con = c.pon()
        print(f'コンピューターの手は{con}です。')
        btl = jj.judge(you, con)
        if btl == "あなたの勝ちです！":
            p_cnt += 1
            print(btl)
        elif btl == "コンピューターの勝ちです！":
            c_cnt += 1
            print(btl)
        else:
            print(btl)
    
    print(f'【最終結果】\nあなた：{p_cnt}勝\nコンピューター：{c_cnt}勝')
    if p_cnt > c_cnt:
        print('あなたの総合勝利です！')
    else:
        print('コンピューターの総合勝利です！')

if __name__ == '__main__':
    janken_main()