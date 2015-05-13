import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *

class Form(QDialog):    # Class ami a QDialogbol orokol
    def __init__(self,parent = None):   #Parent = None az oroklo __init__ nem zavar be
        super(Form,self).__init__(parent)   #felulir

        self.browser = QTextBrowser()       # multi line megjelenito textbrowser gyakorlatilag egy text editor
        self.lineedit = QLineEdit ("Type an expression and press eneter!")  # szoveg ami megjelenik mielott atirjuk
        self.lineedit.selectAll()   #ha beleir az egesz eltunik

        layout = QVBoxLayout()  #rendezze egybe gyakorlatilag ez a doboz amiben megjelenik
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)  #egybol fokuszba veszi a az editalhato reszt nem kell belekattintani

        self.connect(self.lineedit, SIGNAL("returnPressed()"),self.updateUi)    # A linedit (ami egy szovegdoboz) osszekapcsoljuk a return pressdel es ennek hatasara majd updatelia uit
        self.setWindowTitle("Calculate")    #Az ablakon levo szoveget jelenit meg
    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s<b>"% (text,eval(text))) #a beirt szoveg egyenlo a python altal kiszamolt bold szoveggel
        except:
            self.browser.append("<font color = red> %s is invalid</font>" %text)   # Ha az ertek nem adhato ossze stb

app = QApplication(sys.argv)
form = Form()
form.show()     #megjelniti
app.exec_()     #futtatja
