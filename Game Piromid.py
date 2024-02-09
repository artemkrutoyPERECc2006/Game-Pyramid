import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import  uic
from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap
import random
from functools import partial
class MainWindow(QMainWindow):   
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пирамидка")   
        self.count = 0 
        self.k = 0
        self.sel_1 = 0
        self.sel_2 = 0
        self.k1 = 0
        self.k2 = 0
        self.row_s1 = 0
        self.row_s2 = 0
        self.i_s1 = 0 
        self.i_s2  = 0 
        #Создание пирамиды
        self.piromid = []
        start = 0
        for i in range(1,8):
            end = start + i
            self.piromid.append(deck[start:end])
            start = end    
        #Создвние закрытой и открытой стопки
        self.close_card = deck[end:]
        self.open_card = [self.close_card.pop()]
        uic.loadUi('C:\\Users\\Артём\\Documents\\Python\\git game\\view game.ui', self)
        self.ui = uic.loadUi('C:\\Users\\Артём\\Documents\\Python\\git game\\view game.ui', self)
        self.koloda.clicked.connect(self.next_in_koloda)
        self.OpenCard.clicked.connect(self.remove_k)
        self.SumCard.clicked.connect(self.Sum_two_card)
        print(self.k)

        for row in range(len(self.piromid)):
            for i,name in enumerate(piromid_card[row]):
                card = getattr(self.ui, name)
                s = str(self.piromid[row][i][0])+str(self.piromid[row][i][1])
                card.setText(str(s))
                card.clicked.connect(partial(self.proverka, row, i,card))

    #Следующая карта в колоде
    def next_in_koloda(self):
        self.k += 1
        self.steps.setText(f'Количество шагов {self.k}')
        if len(self.open_card) == 0:
            self.open_card = [self.close_card.pop()]
            card = str(self.open_card[0][0])+str(self.open_card[0][1])
            self.OpenCard.setText(f"{card}")
        else:
            self.close_card.insert(0, self.open_card[0])
            self.open_card = [self.close_card.pop()]
            card = str(self.open_card[0][0])+str(self.open_card[0][1])
            self.OpenCard.setText(f"{card}")
    #Удаление короля из колоды
    def remove_k(self):
        self.k += 1
        self.steps.setText(f'Количество шагов {self.k}')
        """Удаление короля из колоды
        """   
        if len(self.open_card) == 0:
            return
        if self.open_card[0][0] == 'K':
            self.open_card.pop()
            self.OpenCard.setText("")
        else:
            if len(self.open_card) == 1:
                self.OpenCard.clicked.connect(self.selected_card_koloda)
    #выбирает карты из колоды
    def selected_card_koloda(self):
        self.k += 1
        self.steps.setText(f'Количество шагов {self.k}')
        if  self.Select_1.text() == "1" and len(self.open_card) != 0:
            card = str(self.open_card[0][0])+str(self.open_card[0][1])
            self.sel_1 = self.open_card.pop()
            self.Select_1.setText(f"{card}")
            self.OpenCard.setText('')
            self.count += 1
            self.k1 += 1 
        else:
            if self.Select_2.text() == "2" and self.count == 1 and len(self.open_card) != 0:
                card = str(self.open_card[0][0])+str(self.open_card[0][1])
                self.sel_2 = self.open_card.pop()
                self.Select_2.setText(f"{card}")
                self.OpenCard.setText('')
                self.k2 += 1
    def proverka(self,row,i,card):
        if self.piromid[row][i][0] == "K":
            self.piromid[row][i] = tuple()
            card.setText('')
            card.setEnabled(False)
            card.hide()
            return
        if row <= len(self.piromid) -1:
            if row == 6:
                card.clicked.connect(partial(self.select_in_pyromid, row,i))
            elif row == 0 and self.piromid[1][0] == tuple() and self.piromid[1][1] == tuple():
                card.clicked.connect(partial(self.select_in_pyromid, row,i))
            elif row == 0 and  i == len(self.piromid[row])-1:
                if (self.piromid[row+3][i] and self.piromid[row+2][i+3] and self.piromid[row+3][i+2]) == True:
                    card.clicked.connect(partial(self.select_in_pyromid, row,i))
            
            elif row == 1 and self.piromid[row+1][i] == tuple() and self.piromid[row+1][i+1] == tuple():
                card.clicked.connect(partial(self.select_in_pyromid, row,i))
            elif row != 1 and i <= len(self.piromid[row])-1:
                if self.piromid[row+1][i] == tuple() and self.piromid[row+1][i+1] == tuple():
                    if row != 0 or i != 0:
                        card.clicked.connect(partial(self.select_in_pyromid, row,i))
           


    def select_in_pyromid(self,row,i):
        self.k += 1
        self.steps.setText(f'Количество шагов {self.k}')
        if self.k1 == 1 and self.Select_1.text() == "1":
            k1 = 0
            self.Select_1.setText("1")
            self.close_card.insert(0, self.sel_1)
            self.sel_1 = 0
        if self.Select_1.text() == "1":
            s = str(self.piromid[row][i][0]) + str(self.piromid[row][i][1])
            self.sel_1 = self.piromid[row][i]
            self.Select_1.setText(s)
            self.i_s1 = i
            self.row_s1 = row
            self.count += 1                   

        elif self.Select_2.text() == "2" and str(self.piromid[row][i][0]) + str(self.piromid[row][i][1]) != self.Select_1.text() and self.count == 1:
            s = str(self.piromid[row][i][0]) + str(self.piromid[row][i][1])
            self.sel_2 = self.piromid[row][i]
            self.Select_2.setText(s)
            self.i_s2 = i
            self.row_s2 = row
            self.count = 0
                    
    def Sum_two_card(self):
        self.k += 1
        self.steps.setText(f'Количество шагов {self.k}')
        if self.sel_1 != 0 and self.sel_2 != 0:
            if dct[self.sel_1[0]] + dct[self.sel_2[0]] == 13:
                if self.k1 == 1:
                    self.piromid[self.row_s2][self.i_s2] = tuple()
                    card1 = getattr(self.ui, piromid_card[self.row_s2][self.i_s2])
                    card1.setEnabled(False)
                    card1.hide()
                    self.Select_1.setText('1')
                    self.Select_2.setText('2')
                    self.k1 = 0
                    self.sel_1 = 0
                    self.count = 0 
                elif self.k2 == 1:
                    self.piromid[self.row_s1][self.i_s1] = tuple()
                    card2 = getattr(self.ui, piromid_card[self.row_s1][self.i_s1])
                    card2.setEnabled(False)
                    card2.hide()
                    self.Select_1.setText('1')
                    self.Select_2.setText('2')
                    self.k2 = 0
                    self.sel_2 = 0
                    self.count = 0
                else:
                    self.piromid[self.row_s1][self.i_s1] = tuple()
                    card1 = getattr(self.ui, piromid_card[self.row_s1][self.i_s1])
                    card1.setEnabled(False)
                    self.piromid[self.row_s2][self.i_s2] = tuple()
                    card2 = getattr(self.ui, piromid_card[self.row_s2][self.i_s2])
                    card2.setEnabled(False)
                    card1.hide()
                    card2.hide()
                    self.Select_1.setText('1')
                    self.Select_2.setText('2')
                    self.k1 = 0
                    self.sel_1 = 0
                    self.k2 = 0
                    self.sel_2 = 0
                    self.count = 0
            else:
                if self.k1 == 1:
                    self.close_card.insert(0, self.sel_1)
                    self.sel_1 = 0
                    self.k1 = 0
                    self.Select_1.setText("1")
                    self.Select_2.setText("2")
                    self.count = 0
                elif self.k2 == 1:
                    self.close_card.insert(0, self.sel_2)
                    self.sel_2 = 0
                    self.k2 = 0
                    self.Select_1.setText("1")
                    self.Select_2.setText("2")
                    self.count = 0
                else:
                    self.sel_1 = 0
                    self.k2 = 0
                    self.sel_1 = 0
                    self.sel_2 = 0
                    self.Select_1.setText("1")
                    self.Select_2.setText("2") 
                    self.count = 0

suits = ['♠️', '♥️', '♦️', '♣️']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for rank in ranks for suit in suits]
dct = {'A': 1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
random.shuffle(deck)




#Создание списка кард
cards = []
for i in range(1,29):
    cards.append(f"Card_{i}")
    j = 1
#Создание пирамиды карт
piromid_card = []
start = 0
for i in range(1,8):
    end = start + i
    piromid_card.append(cards[start:end])
    start = end
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()