import sys


class Calc:
    def __init__(self):
        pass

    def data_input(self):
        print('chara?')
        self.chara_atk = int(sys.stdin.readline())
        print('weapon?')
        self.weapon_atk = int(sys.stdin.readline())
        print('weapon_percent?')
        self.weapon_percent = int(sys.stdin.readline())
        print('accessory?')
        self.accessory_atk = int(sys.stdin.readline())
        print('accessory_percent?')
        self.accessory_percent = int(sys.stdin.readline())

    def basic_atk(self):  # 基礎攻撃力+聖遺物+武器%上昇
        base = self.chara_atk + self.weapon_atk  # キャラ攻撃力+武器攻撃力
        accessory = base * (self.accessory_percent / 100) + self.accessory_atk  # ベース*アクセ倍率+アクセサブステ攻撃力
        weapon = (base * self.weapon_percent / 100)  # ベース*武器倍率
        tmp = base + accessory + weapon
        return tmp

    def data_get(self):
        print(self.chara_atk)
        print(self.weapon_atk)


def main():
    calc = Calc()
    calc.data_input()
    calc.data_get()


if __name__ == '__main__':
    main()
