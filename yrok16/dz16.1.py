class Cassa(object):

    __money = 0

    def top_up(self, x):
        self.__money += x
    
    def count_1000(self):
        print(self.__money // 1000)
    
    def take_away(self, x):
        if x < self.__money:
            took = self.__money - x
            print(f"Взял {took} денег")
        else:
            print("Недостаточно денег")