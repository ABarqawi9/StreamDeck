# i commited this 
import os
import sys
import subprocess
from getpass import getpass
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class StreamDeck(QWidget):
    def __init__(self):
        super().__init__()

        #self.setWindowIcon(QtGui.QIcon('Python\Example.png'))
        
        # Create buttons
        self.button1 = QPushButton("Discord", self)
        self.button2 = QPushButton('Spotify', self)
        self.button3 = QPushButton('MS Edge', self)
        self.button4 = QPushButton('Google Chrome', self)
        self.button5 = QPushButton('Steam', self)

        # Set button styles with QSS
        button_style = '''
    QPushButton {
        background-color: #301934;
        color: #ecf0f1;
        border-style: solid;
        border-width: 2px;
        border-color: #ecf0f1;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #4e2854;
        border-color: #fcfcfc;
    }
    QPushButton:pressed {
        background-color: #00FF00;
        border-color: #2980b9;
    }
'''

        self.setStyleSheet(button_style)

        # Connect button signals to slots
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)
        
        # Set up layout
        layout = QGridLayout()
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0)
        layout.addWidget(self.button4, 1, 1)
        layout.addWidget(self.button5, 2, 0)
        self.setLayout(layout)


    # Define slot functions
    def button1_clicked(self):
        user = os.getlogin()
        subprocess.Popen(f'C:\\Users\\{user}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe')

    def button2_clicked(self):
        user = os.getlogin()
        subprocess.Popen(f'C:\\Users\\{user}\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe --processStart Spotify.exe')

    def button3_clicked(self):
        user = os.getlogin()
        subprocess.Popen(f'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        
    def button4_clicked(self):
        user = os.getlogin()
        subprocess.Popen(f'C:\Program Files\Google\Chrome\Application\chrome.exe')
        
    def button5_clicked(self):
        user = os.getlogin()
        subprocess.Popen(f'C:\Program Files (x86)\Steam\steam.exe')
        

if __name__ == '__main__':
    # Create the application and show the GUI
   # print(os.listdir('Python'))
    app = QApplication(sys.argv) 
    app.setApplicationDisplayName('Virtual Stream Deck')
    streamdeck = StreamDeck()
    streamdeck.show()
    sys.exit(app.exec_())
    
