from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator
import sys
import sudoku



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self .setWindowTitle('Sudoku')
        self.Central=QWidget(self)
        self.setCentralWidget(self.Central)
        self.setFixedSize(480,640)
        self.layout()
        self.signal()
    def layout(self):
        layout=QVBoxLayout()
        self.Central.setLayout(layout)
        self.text={}
        grid=QGridLayout()
        for i in range(81):
            self.text[i]=QLineEdit()
            self.text[i].setFixedSize(50,50)
            self.text[i].setAlignment(QtCore.Qt.AlignCenter)
            font=self.text[i].font()
            font.setPointSize(16)
            self.text[i].setFont(font)
            self.text[i].setMaxLength(1)
            val=QIntValidator()
            self.text[i].setValidator(val)
            if i in (0,8,72,80):
                pass
            elif  i in (2,5):
                self.text[i].setStyleSheet("border : solid black;""border-width : 4px 2px 1px 1px;")
            elif i in (3,6):
                self.text[i].setStyleSheet("border : solid black;""border-width : 4px 1px 1px 2px;")
            elif i in (74,77):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 2px 4px 1px;")
            elif i in (75,78):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 4px 2px;")
            elif i in (18,45):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 2px 4px;")
            elif i in (26,53):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 4px 2px 1px;")
            elif i in (27,54):
                self.text[i].setStyleSheet("border : solid black;""border-width : 2px 1px 1px 4px;")
            elif i in (35,62):
                self.text[i].setStyleSheet("border : solid black;""border-width : 2px 4px 1px 1px;")
            elif i<8:
                self.text[i].setStyleSheet("border : solid black;""border-width : 4px 1px 1px 1px;")
            elif i%9 == 0:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 1px 4px;")
            elif i%9==8:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 4px 1px 1px;")
            elif i>72 and i <80:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 4px 1px;")
            elif i in (20,23,47,50):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 2px 2px 1px;")
            elif i in (21,24,48,51):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 2px 2px;")
            elif i in (29,32,56,59):
                self.text[i].setStyleSheet("border : solid black;""border-width : 2px 2px 1px 1px;")
            elif i in (30,33,57,60):
                self.text[i].setStyleSheet("border : solid black;""border-width : 2px 1px 1px 2px;")
            elif i%9==2 or i%9==5:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 2px 1px 1px;")
            elif i%9==3 or i%9==6:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 1px 2px;")
            elif (i >18 and i<26) or (i>45 and i<53):
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 2px 1px;")
            elif (i>27 and i<35) or (i>54 and i<62):
                self.text[i].setStyleSheet("border : solid black;""border-width : 2px 1px 1px 1px;")
            else:
                self.text[i].setStyleSheet("border : solid black;""border-width : 1px 1px 1px 1px;")
        k=0
        self.text[0].setStyleSheet("border : solid black;""border-width : 4px 1px 1px 4px;")
        self.text[8].setStyleSheet("border : solid black;""border-width : 4px 4px 1px 1px;")
        self.text[72].setStyleSheet("border : solid black;""border-width : 1px 1px 4px 4px;")
        self.text[80].setStyleSheet("border : solid black;""border-width : 1px 4px 4px 1px;")
        for i in range(9):
            for j in range(9):
                grid.addWidget(self.text[k],i,j)
                k+=1
        grid.setSpacing(0)
        self.clear=QPushButton('Clear')
        self.solve=QPushButton('Solve')
        buttons=QHBoxLayout()
        buttons.addWidget(self.solve)
        buttons.addWidget(self.clear)
        layout.addLayout(grid)
        layout.addLayout(buttons)
    def signal(self):
        self.solve.clicked.connect(self.get)
        self.clear.clicked.connect(self.delete)
    def get(self):
        L=[[],[],[],[],[],[],[],[],[]]
        i=0
        while i!=81:
            for j in range(9):
                for k in range(9):
                    if self.text[i].text() !='':
                        L[j].append(int(self.text[i].text()))
                    else:
                        L[j].append(0)
                    i+=1
        result=sudoku.solve(L)
        i=0
        for j in range(9):
            for k in range(9):
                self.text[i].setText(str(result[j][k]))
                i+=1
    def delete(self):
        for i in range(81):
            self.text[i].setText('')
def main():
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
main()