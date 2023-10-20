#importing the component we need
from PySide6.QtWidgets import QApplication, QWidget

#SYS: Procces comand line arguments to pick up by QAPP
import sys

#run the aplicattion and wait the thing to happend
app=QApplication(sys.argv)

#window are hidden by default
window=QWidget()
#show the hidden window
window.show()
#waiting the things to happend  (Event loop catching)
app.exec()  #Start de event loop
#app.exec_() #This will be removed , do not use