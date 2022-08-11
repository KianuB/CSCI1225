from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from view import Ui_MainWindow
import random
# QTimer is used to add a delay between resets due to the sleep method freezing the GUI
# random is used to determine computer moves

# global variables used for available moves and tracking turn
options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 'X'

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # clicking an available space will call the corresponding function
        self.pushButton_1.clicked.connect(lambda: self.play_1('X'))
        self.pushButton_2.clicked.connect(lambda: self.play_2('X'))
        self.pushButton_3.clicked.connect(lambda: self.play_3('X'))
        self.pushButton_4.clicked.connect(lambda: self.play_4('X'))
        self.pushButton_5.clicked.connect(lambda: self.play_5('X'))
        self.pushButton_6.clicked.connect(lambda: self.play_6('X'))
        self.pushButton_7.clicked.connect(lambda: self.play_7('X'))
        self.pushButton_8.clicked.connect(lambda: self.play_8('X'))
        self.pushButton_9.clicked.connect(lambda: self.play_9('X'))

    # for each played space, the text is changed to the player that chose it and then disabled
    # after making space unplayable, runs check function to check for game end
    def play_1(self, player):
        self.pushButton_1.setCheckable(False)
        self.pushButton_1.setEnabled(False)
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setText(player)
        options.remove(1)
        self.check()

    def play_2(self, player):
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setText(player)
        options.remove(2)
        self.check()

    def play_3(self, player):
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setText(player)
        options.remove(3)
        self.check()

    def play_4(self, player):
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setText(player)
        options.remove(4)
        self.check()

    def play_5(self, player):
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setText(player)
        options.remove(5)
        self.check()

    def play_6(self, player):
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setText(player)
        options.remove(6)
        self.check()

    def play_7(self, player):
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setText(player)
        options.remove(7)
        self.check()

    def play_8(self, player):
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setText(player)
        options.remove(8)
        self.check()

    def play_9(self, player):
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setText(player)
        options.remove(9)
        self.check()

    # chooses a random available space for computer to play
    # potential future addition: difficulty select (finds best move for computer)
    def play_computer(self):
        move = random.choice(options)
        if move == 1:
            self.play_1('O')
        elif move == 2:
            self.play_2('O')
        elif move == 3:
            self.play_3('O')
        elif move == 4:
            self.play_4('O')
        elif move == 5:
            self.play_5('O')
        elif move == 6:
            self.play_6('O')
        elif move == 7:
            self.play_7('O')
        elif move == 8:
            self.play_8('O')
        elif move == 9:
            self.play_9('O')

    # checks each possible win condition or tie game, then proceeds to next turn
    def check(self):
        global options
        if self.pushButton_1.text() == 'X' and self.pushButton_2.text() == 'X' and self.pushButton_3.text() == 'X':
            self.win('X')
        elif self.pushButton_4.text() == 'X' and self.pushButton_5.text() == 'X' and self.pushButton_6.text() == 'X':
            self.win('X')
        elif self.pushButton_7.text() == 'X' and self.pushButton_8.text() == 'X' and self.pushButton_9.text() == 'X':
            self.win('X')
        elif self.pushButton_1.text() == 'X' and self.pushButton_4.text() == 'X' and self.pushButton_7.text() == 'X':
            self.win('X')
        elif self.pushButton_2.text() == 'X' and self.pushButton_5.text() == 'X' and self.pushButton_8.text() == 'X':
            self.win('X')
        elif self.pushButton_3.text() == 'X' and self.pushButton_6.text() == 'X' and self.pushButton_9.text() == 'X':
            self.win('X')
        elif self.pushButton_1.text() == 'X' and self.pushButton_5.text() == 'X' and self.pushButton_9.text() == 'X':
            self.win('X')
        elif self.pushButton_3.text() == 'X' and self.pushButton_5.text() == 'X' and self.pushButton_7.text() == 'X':
            self.win('X')
        elif self.pushButton_1.text() == 'O' and self.pushButton_2.text() == 'O' and self.pushButton_3.text() == 'O':
            self.win('O')
        elif self.pushButton_4.text() == 'O' and self.pushButton_5.text() == 'O' and self.pushButton_6.text() == 'O':
            self.win('O')
        elif self.pushButton_7.text() == 'O' and self.pushButton_8.text() == 'O' and self.pushButton_9.text() == 'O':
            self.win('O')
        elif self.pushButton_1.text() == 'O' and self.pushButton_4.text() == 'O' and self.pushButton_7.text() == 'O':
            self.win('O')
        elif self.pushButton_2.text() == 'O' and self.pushButton_5.text() == 'O' and self.pushButton_8.text() == 'O':
            self.win('O')
        elif self.pushButton_3.text() == 'O' and self.pushButton_6.text() == 'O' and self.pushButton_9.text() == 'O':
            self.win('O')
        elif self.pushButton_1.text() == 'O' and self.pushButton_5.text() == 'O' and self.pushButton_9.text() == 'O':
            self.win('O')
        elif self.pushButton_3.text() == 'O' and self.pushButton_5.text() == 'O' and self.pushButton_7.text() == 'O':
            self.win('O')
        elif len(options) == 0:
            QTimer.singleShot(1000, self.reset)

        else:
            global turn
            if turn == 'X':
                turn = 'O'
                self.play_computer()
            else:
                turn = 'X'

    # gives the winner 1 point and disables all spaces during 1 sec wait period before reset
    def win(self, player):
        if player == 'X':
            score = int(self.label_player_score.text())
            score += 1
            self.label_player_score.setText(str(score))
        elif player == 'O':
            score = int(self.label_computer_score.text())
            score += 1
            self.label_computer_score.setText(str(score))

        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        QTimer.singleShot(1000, self.reset)

    # resets all spaces to their original state, restoring all options for the computer moves
    # ensures player starts every game
    def reset(self):
        global options
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        global turn
        turn = 'X'
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setText('1')
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setText('2')
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setText('3')
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setText('4')
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setText('5')
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setText('6')
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setText('7')
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setText('8')
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setText('9')
