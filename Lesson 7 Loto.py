import random
#===================================================================================
class Card:
    def __init__(self, name, card = []):
        self.card = card
        self.name = name
        self.card = random.sample(range(1, 90), 15)
        self.card_show()        
      
    def card_check(self, lap):
        self.card_show()
        for el in self.card:
            if el == keg:
                self.card.remove(el)
                print("Номер {} обнаружен в карточке и зачеркнут!".format(keg))

        if len(self.card) == 0:
            print("\nКАРТОЧКА ЗАКРЫТА.\nПОБЕДИТЕЛЬ: ", self.name)
            lap = 91
        return lap

    def card_show(self):
        print("\nКарточка игрока: ",self.name)
        print("-"*65)
        print(self.card)
        print("-"*65)
        
#===================================================================================
def continue_game():
    quest = ""
    while (quest != "n") and (quest != "y"):
        quest = str(input("\n\n{:>35s}".format("Продолжить (y-да, n-нет)? y/n: ")))
    return quest
#===================================================================================

print("ИГРА     __   ___   __ ")
print("   /\   |  |   |   |  |")
print("  /  \  |  |   |   |  |")
print(" /    \ |__|   |   |__|")
print("=================================================================\n")

name_user = input("Введите Ваше имя: ")

print("\n-------------------------НАЧИНАЕМ ИГРУ!--------------------------\n")
print("  ...заполняем мешок бочонками...\n")
print("  ...перемешиваем мешок...\n")
print("  ...раздаем карточки...")

#Заполним мешок бочонками и перемешаем его
#box - мешок с бочонками
#keg - бочонок

box = [i for i in range(1, 91)]
keg = 0

#Сформируем карты игроков
card_user = Card(name_user.upper())
card_PC = Card("КОМПЬЮТЕР")

print("\n=================================================================\n")

lap = 0
while lap < 90:

    random.shuffle(box) #перемешиваем бочонки в мешке
    keg = box[0]
    box.pop(0)
    last_lap = lap

    print("\nКРУГ №: {}".format(lap + 1))
    print("Достаем новый бочонок из мешка: {} (осталось бочонков: {})".format(keg, str(len(box))))

    t = card_PC.card_check(lap)
    if t != lap:
        break
    t = card_user.card_check(lap)
    if t != lap:
        break

    print("*"*65)    
    quest = continue_game()#проверяем, хотим ли играть дальше
    if quest == "n":
        lap = 91
    lap += 1
    print("\n\n" + "*"*65)
    
print("\nОставшиеся бочонки в мешке:\n{}".format(box))
print("\n-------------------------ИГРА ЗАВЕРШЕНА!-------------------------\n")

