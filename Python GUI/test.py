import sys
from PySide.QtCore import *  # minden functiont importal
from PySide.QtGui import * # ez felelos a kepernyo projekcioert
import time

app = QApplication (sys.argv)   # Ehhez kell a sys module az elso argument barmelyi kpython filenal a file helye


try:
    due = QTime.currentTime()   #Lekeri az idot
    message = "Alert!"

    if len(sys.argv) < 2:   #Az app mukodesehez minimum ket argument kell az elso az alap a file neve a masodik argument amikorra az ertesitest keri
        raise ValueError

    hours,minutes = sys.argv[1].split(":")  #A sys masodik argumentjet veszi es mivel idopont pl 15:30 a 15-t a hourba a 30-at a minutes varaible menti (split return a list)
    due = QTime ((int(hours)), int(minutes))  #A QTime function felvesz ket arguemntet de ezeket intbe kell alakitani mivel a split listet csinalt

    if not due.isValid():   # A Qtime classnak van egy isvalid classa ami ellenorzi az erteket ha nem igaz --> Raise value --> leall
        raise ValueError

    if len(sys.argv) > 2:   # Ha az argument tobb mint 2
        message = " ".join(sys.argv[2:])    # Ha az argumentben tobb ertek is van pl 15:40 This is my message akkor a tobbi erteket a szokozoknel joinolja egy stringe
except ValueError:
    message = "Usage: firstTutorial.py HH:mm [optional message]"    # 24 hour clock

while QTime.currentTime()< due:    # Ha a jelenlegi ido kisebb mint a megadott akkor var 10 secet
    time.sleep(10)

label = QLabel("<font color = red size = 72><b>" + message + "</b></font>")    # A label az az elem ami fixen ki van irva egy helyre a guin a QLabel htm tageket fogad be
label.setWindowFlags(Qt.SplashScreen)   #Splashscreen ami megjelenik amikor a program tolt
label.show()

QTimer.singleShot(20000,app.quit)   # singleshot = egyszer ismetelje , elso elem a signal = var 20000 secet aztan aktivalja a masodik felet app.quit  ami bezarja az appot
app.exec_() #elinditja az appot