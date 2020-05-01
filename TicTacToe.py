import random
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class Homescreen(Screen):
    def changer_game(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

    def singleplayer_mode(self):
        Game.computer = True
        self.changer_game()

    def multiplayer(self):
        Game.mehrspieler = True
        self.changer_game()

class Game(Screen):
    i = 0
    dic = {"row_1": {"pos1": "LEER", "pos2": "LEER", "pos3": "LEER"},
           "row_2": {"pos4": "LEER", "pos5": "LEER", "pos6": "LEER"},
           "row_3": {"pos7": "LEER", "pos8": "LEER", "pos9": "LEER"}}
    variante_3_a1 = 0
    variante_3_a2 = 0
    variante_3_b1 = 0
    variante_3_b2 = 0
    computer = False
    singleplayer = False
    offen = False
    mehrspieler = False

    def varianten(self):
        self.variante_3_a1 = 0
        self.variante_3_a2 = 0
        self.variante_3_b1 = 0
        self.variante_3_b2 = 0

    def changer_login(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
        self.remove_images()

    def reset_dic(self):
        self.dic = {"row_1": {"pos1": "LEER", "pos2": "LEER", "pos3": "LEER"},
                    "row_2": {"pos4": "LEER", "pos5": "LEER", "pos6": "LEER"},
                    "row_3": {"pos7": "LEER", "pos8": "LEER", "pos9": "LEER"}}

    # singleplayer vs computer
    def player_com(self):
        if self.mehrspieler == False:
            if self.computer == True:
                x = random.randint(1, 9)
                if x == 1:
                    self.pos_1()
                elif x == 2:
                    self.pos_2()
                elif x == 3:
                    self.pos_3()
                elif x == 4:
                    self.pos_4()
                elif x == 5:
                    self.pos_5()
                elif x == 6:
                    self.pos_6()
                elif x == 7:
                    self.pos_7()
                elif x == 8:
                    self.pos_8()
                elif x == 9:
                    self.pos_9()
                else:
                    pass

    # win ?
    def game_won(self):
        self.variante_2 = [0, 0, 0]
        for row, item in self.dic.items():
            self.zahl = 0
            self.winning_count_a = 0
            self.winning_count_b = 0
            # check variante 1, 2 und 3
            for i in item.values():
                if i == 1:
                    self.winning_count_a += 1
                    self.variante_2[self.zahl] += 1.1
                if i == 0:
                    self.winning_count_b += 1
                    self.variante_2[self.zahl] += 2
                if self.winning_count_a == 3 or round(self.variante_2[0], 2) == 3.3 or round(self.variante_2[1],
                                                                                             2) == 3.3 or round(
                    self.variante_2[2], 2) == 3.3 or self.variante_3_a1 == 3 or self.variante_3_a2 == 15:
                    Winning_Popup.gewonnen(self, 1)
                    self.varianten()
                elif self.winning_count_b == 3 or self.variante_2[0] == 6 or self.variante_2[1] == 6 or self.variante_2[
                    2] == 6 or self.variante_3_b1 == 3 or self.variante_3_b2 == 15:
                    Winning_Popup.gewonnen(self, 0)
                    self.varianten()
                self.zahl += 1

    # tauscht kreis / kreuz
    def player1_or_player2(self):
        if self.i % 2 == 0:
            self.i += 1
            self.was_ist_es = 0
            self.singleplayer = True
            return "kreis.png"

        else:
            self.i += 1
            self.was_ist_es = 1
            self.singleplayer = False
            return "cross.png"

    def remove_images(self):
        self.varianten()
        self.zahl = 1
        self.offen = False
        self.i = 0
        for i in self.dic:
            for lol in self.dic[i]:
                x = "pos" + str(self.zahl)
                if self.zahl < 4:
                    if x == "pos1":
                        if self.dic["row_1"][x] != "LEER":
                            self.remove_widget(self.pos1)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos2":
                        if self.dic["row_1"][x] != "LEER":
                            self.remove_widget(self.pos2)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos3":
                        if self.dic["row_1"][x] != "LEER":
                            self.remove_widget(self.pos3)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    else:
                        self.zahl += 1
                        continue
                elif self.zahl < 7:
                    if x == "pos4":
                        if self.dic["row_2"][x] != "LEER":
                            self.remove_widget(self.pos4)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos5":
                        if self.dic["row_2"][x] != "LEER":
                            self.remove_widget(self.pos5)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos6":
                        if self.dic["row_2"][x] != "LEER":
                            self.remove_widget(self.pos6)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    else:
                        self.zahl += 1
                        continue
                else:
                    if x == "pos7":
                        if self.dic["row_3"][x] != "LEER":
                            self.remove_widget(self.pos7)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos8":
                        if self.dic["row_3"][x] != "LEER":
                            self.remove_widget(self.pos8)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    elif x == "pos9":
                        if self.dic["row_3"][x] != "LEER":
                            self.remove_widget(self.pos9)
                            self.zahl += 1
                        else:
                            self.zahl += 1
                    else:
                        self.zahl += 1
                        continue
        self.dic = {"row_1": {"pos1": "LEER", "pos2": "LEER", "pos3": "LEER"},
                    "row_2": {"pos4": "LEER", "pos5": "LEER", "pos6": "LEER"},
                    "row_3": {"pos7": "LEER", "pos8": "LEER", "pos9": "LEER"}}
        self.x = "1"

    def variante_3_check_1(self):
        if self.was_ist_es == 1:
            self.variante_3_a1 += 1
        else:
            self.variante_3_b1 += 1

    def variante_3_check_2(self):
        if self.was_ist_es == 1:
            self.variante_3_a2 += 5
        else:
            self.variante_3_b2 += 5

    def computer_check_action(self):
        if self.singleplayer == True:
            self.computer = True
            self.player_com()
            self.singleplayer = False

    def pos_1(self):
        try:
            if self.dic["row_1"]["pos1"] == "LEER":
                self.pos1 = Image(source=self.player1_or_player2(), pos=(-200, 210))
                self.add_widget(self.pos1)
                self.variante_3_check_1()
                self.dic["row_1"]["pos1"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_2(self):
        try:
            if self.dic["row_1"]["pos2"] == "LEER":
                self.pos2 = Image(source=self.player1_or_player2(), pos=(0, 210))
                self.add_widget(self.pos2)
                self.dic["row_1"]["pos2"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_3(self):
        try:
            if self.dic["row_1"]["pos3"] == "LEER":
                self.pos3 = Image(source=self.player1_or_player2(), pos=(200, 210))
                self.add_widget(self.pos3)
                self.variante_3_check_2()
                self.dic["row_1"]["pos3"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_4(self):
        try:
            if self.dic["row_2"]["pos4"] == "LEER":
                self.pos4 = Image(source=self.player1_or_player2(), pos=(-200, 60))
                self.add_widget(self.pos4)
                self.dic["row_2"]["pos4"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_5(self):
        try:
            if self.dic["row_2"]["pos5"] == "LEER":
                self.pos5 = Image(source=self.player1_or_player2(), pos=(0, 60))
                self.add_widget(self.pos5)
                if self.was_ist_es == 1:
                    self.variante_3_a1 += 1
                    self.variante_3_a2 += 5
                else:
                    self.variante_3_b1 += 1
                    self.variante_3_b2 += 5
                self.dic["row_2"]["pos5"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_6(self):
        try:
            if self.dic["row_2"]["pos6"] == "LEER":
                self.pos6 = Image(source=self.player1_or_player2(), pos=(200, 60))
                self.add_widget(self.pos6)
                self.dic["row_2"]["pos6"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_7(self):
        try:
            if self.dic["row_3"]["pos7"] == "LEER":
                self.pos7 = Image(source=self.player1_or_player2(), pos=(-200, -90))
                self.add_widget(self.pos7)
                self.variante_3_check_2()
                self.dic["row_3"]["pos7"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_8(self):
        try:
            if self.dic["row_3"]["pos8"] == "LEER":
                self.pos8 = Image(source=self.player1_or_player2(), pos=(0, -90))
                self.add_widget(self.pos8)
                self.dic["row_3"]["pos8"] = self.was_ist_es
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass

    def pos_9(self):
        try:
            if self.dic["row_3"]["pos9"] == "LEER":
                self.pos9 = Image(source=self.player1_or_player2(), pos=(200, -90))
                self.add_widget(self.pos9)
                self.dic["row_3"]["pos9"] = self.was_ist_es
                self.variante_3_check_1()
                self.game_won()
                self.computer_check_action()
            else:
                self.computer_check_action()
        except RecursionError:
            pass


class Winning_Popup(Popup):
    def gewonnen(self, player):
        if self.offen == False:
            if player == 1:
                x = "X"
            else:
                x = "O"
            WinningLabel.text = "Player " + x + " has WON!"
            popup = Winning_Popup()
            popup.open()
            self.offen = True


class FullImage(Image):
    pass


class WinningLabel(Label):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("tic.kv")


class TicTacToe(App):
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = Homescreen()
        screen2 = Game()
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        return my_screenmanager


if __name__ == "__main__":
    TicTacToe().run()
