import random
suits = ['♠️', '♥️', '♦️', '♣️']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for rank in ranks for suit in suits]
dct = {'A': 1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
random.shuffle(deck)
#Создание пирамиды
piromid = []
start = 0
for i in range(1,8):
    end = start + i
    piromid.append(deck[start:end])
    start = end

#Создвние закрытой и открытой стопки
close_card = deck[end:]
open_card = [close_card.pop()]
def print_piramid():
    #Вывод пирамиды повторно
    print("Пирамида:")
    for i in piromid:
        print(*i)
#Функционал игры
def koloda():
    card = str(*open_card)
    print(f'\nКоличество карт в колоде {len(close_card)} \n\nОткрытая крта {card}\n')
def proverka(row:int,i:int) -> bool:
    """
    Функция, которая проверяет можно достать карту из колоды 
    Args:
        row (int):  Строка пирамиды
        i (int): Индекс карты в строке
    """
    if row <= len(piromid) -1:
        if row == 6:
            return True
        elif row == 0 and  i == len(piromid[row])-1:
            if (piromid[row+2][i] and piromid[row+2][i+1] and piromid[row+2][i+2]) == True:
                return True
        elif row != 1 and i <= len(piromid[row])-1:
            if piromid[row+1][i] == '   None   ' and piromid[row+1][i+1] == '   None   ':
                return True
    return False
        
        
    
def remove_card(row: int,i:int):
    """Функция  для удаления карты из пирамиды
    Args:
        row (int): Номер строки в пирамиде
        i (int): Индекс  карты в строке
    """
    if proverka(row,i):
        piromid[row][i] = '   None   '
def next_in_koloda():
    global open_card
    global close_card
    if len(open_card) == 0:
        open_card = [close_card.pop()]
    else:
        close_card.insert(0, open_card[0])
        open_card = [close_card.pop()]
    print(close_card)
def stack_two_card(row:int,i: int, row2:int, i2:int):
    """Функция складывает две карты 
    и если сумма их значений == 13 удаляет их
    Args:
    row1 (int): Номер первой строки
    i1 (int): Индекс карты на первой строке
    row2 (int): Номер второй строки
    i2 (int): Индекс карты на второй строки
    """
    if dct[piromid[row][i][0]] + dct[piromid[row2][i2][0]] == 13:
        remove_card(row,i)
        remove_card(row2,i2)
    else:
        print("Неверные карты")
def sum_koloda_and_piramida(row,i,card_k):
    global open_card
    global close_card
    """Складывает карту из колоды с картой из пирамиды"""
    if dct[piromid[row][i][0]] + dct[card_k[0]] == 13:
        remove_card(row,i)
        open_card.pop()
    else:
        print('Карты сложить нельзя')
def remove_k():
    global open_card
    global close_card
    """Удаление короля из колоды
    """   
    if open_card[0][0] == 'K':
        print('sdf')
        open_card.pop()
        print('Король удален')
    else:
        print('Карта не является королем')
#Игра
while True:
    #Выбор  действий пользователя
    print_piramid()
    action = int(input(""" Действия:\n1.Выход\n2.Показать колоду\n3.Следующая карта в колоде\n4.Сделать ход\n5.Удалить короля из колоды\n"""))
    if action == 1:
        break
    elif action == 2:
        koloda()
    elif action == 3:
        next_in_koloda()
        koloda()
    elif action == 4:
        row = int(input('Введите номер строки(0-6)'))
        i =  int(input(f'Введите индекс карты (0-{len(piromid[row])})'))
        if proverka(row, i) == True:
            if piromid[row][i][0] == 'K':
                piromid[row][i] = '   None   '
                continue
            else:
                action2 = int(input("""Выберите дейсятвие:
                1.Сложение карт из пирамиды
                2.Сложить карту с картой  из колоды\n
                """))
                if action2 == 1:
                    row2 = int(input('Введите номер второй строки'))
                    i2 = int(input(f'Введите индекс второй карты (0-{row2-1})'))
                    if proverka(row2, i2) == True:
                        if stack_two_card(row,i, row2,i2):
                            remove_card(row,i)
                            remove_card(row2,i2)
                    else:
                        print('Введены неверные координаты')
                        continue
                elif action2 == 2:
                    if dct[open_card[0][0]] == "K":
                        open_card.pop()
                    else:
                        card = open_card[0]
                        sum_koloda_and_piramida(row, i, card)
                else:
                    print('Нет такого действия')
                    continue       
    elif action == 5:
        remove_k()
    if piromid[0] == '   None   ':
        print('ПОБЕДА!!!!')
        break
    print('\n')
    
        
    
