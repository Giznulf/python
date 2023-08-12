pets = dict()

n = int(input("Введите колличество питомцев: "))

for i in range(n):
    print("Введите имя питомца:")
    name = input()
    if name in pets.keys():
        ret = input("Такой питомец уже есть в списке, заменить? (есди надо заменить введите 'Да'): ")
        if ret != "Да":
            continue
    print("Введите вид питомца")
    view = input()
    print("Введите возраст питомца")
    age = int(input())
    print("Введите имя владельца")
    boss = input()
    pets[name] = {
        "Вид питомца": view,
        "Возраст питомца": age,
        "Имя владельца": boss}

for pet in pets.keys():
    age = pets[pet]['Возраст питомца']
    wordForm = "лет"
    if (age != 11) and (age != 12) and (age != 13) and (age != 14) :
        if ((age % 10) == 1):
             wordForm = "год"
        elif ((age % 10) == 2) or ((age % 10) == 3) or ((age % 10) == 4):
             wordForm = "года"
        else:
             wordForm = "лет"
    print(F"Это {pets[pet]['Вид питомца']} по кличке {pet} Возраст питомца: {age} {wordForm}. Имя владельца: {pets[pet]['Имя владельца']}")