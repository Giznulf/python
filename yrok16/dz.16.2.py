import math

class Turtle(object):
    x = 0
    y = 0
    s = 0

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self): #- увеличивает y на s
        self.y += self.s
        self.__Good(self.x, self.y)

    def go_down(self): #- уменьшает y на s
        if (self.y - self.s) < 0:
            self.__Bad()
        else:
            self.y -= self.s
            self.__Good(self.x, self.y)

    def go_left(self): #- уменьшает x на s
        if (self.x - self.s) < 0:
            self.__Bad()
        else:
            self.x -= self.s
            self.__Good(self.x, self.y)

    def go_right(self): #- увеличивает y на s
        self.x += self.s
        self.__Good(self.x, self.y)

    def evolve(self): #- увеличивает s на 1
        self.s += 1

    def degrade(self): #- уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s > 1:
            self.s -= 1
        else:
            print("Расстояние которое может пройти черепашка за ход не может быть меньше 1")

    def count_moves(self, x2, y2): # - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        i = self.x - x2
        j = self.y - y2

        result = math.ceil((abs(i) + abs(j)) / self.s)

        print(f"Вам необходимо минимум {result} шагов с текущей скоростью чтобы достигнуть {x2}x{y2}")

    def __Bad(self):
        print("Черепашка не может так двигаться потому что уйдет за край поля")

    def __Good(self, x, y):
        print(f"Черепашка на позиции {x}x{y}")
