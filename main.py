from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from youtube_dl import YoutubeDL
import os
import pyautogui as pg

class MP4(QMainWindow):
    def __init__(self):
        super(MP4, self).__init__()
        self.setGeometry(500, 200, 1000, 600)
        self.setWindowTitle("YouTube Converter")
        self.setWindowIcon(QIcon('youtube.png'))
        self.setStyleSheet('background: #F0F8FF')
        self.UI()
    
    def UI(self):
        self.link = QLineEdit(self)
        self.link.move(240, 215)
        self.link.setFixedHeight(50)
        self.link.setFixedWidth(550)
        self.link.setStyleSheet("background: #FFFAFA; border: 1px solid black; color: solid black; border-radius: 4px; font: 13pt")
        self.link.setPlaceholderText("Insert a YouTube video URL here..")

        self.label = QLabel('Download MP4', self)
        self.label.move(410, 125)
        self.label.setStyleSheet("color: solid black; font: 22pt")
        self.label.adjustSize()

        self.button = QPushButton('Convert', self)
        self.button.move(430, 290)
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(150)
        self.button.setStyleSheet("background: #A52A2A; color: white; border: 1px solid black; border-radius: 4px; font: 10pt; font: 13pt")
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        try:
            mp4_path = os.path.join(os.environ['USERPROFILE'],"Desktop")
            os.chdir(f"{mp4_path}")
            os.mkdir("MP4 Files")
            os.chdir(f'{mp4_path}\MP4 Files')
            
            self.video_downloder = YoutubeDL({'format':'mp4'})
            new = self.link.text()
            self.video_downloder.extract_info(new)
        
        except FileExistsError:
            os.chdir(f'{mp4_path}\MP4 Files')
            self.video_downloder = YoutubeDL({'format':'mp4'})
            new = self.link.text()
            self.video_downloder.extract_info(new)
        
class MP3(QMainWindow):
    def __init__(self):
        super(MP3, self).__init__()
        self.setGeometry(500, 200, 1000, 600)
        self.setWindowTitle("YouTube Converter")
        self.setWindowIcon(QIcon('youtube.png'))
        self.setStyleSheet('background: #F0F8FF')
        self.UI()
    
    def UI(self):
        self.link = QLineEdit(self)
        self.link.move(240, 215)
        self.link.setFixedHeight(50)
        self.link.setFixedWidth(550)
        self.link.setStyleSheet("background: #FFFAFA; border: 1px solid black; color: solid black; border-radius: 4px; font: 13pt")
        self.link.setPlaceholderText("Insert a YouTube video URL here..")

        self.label = QLabel('Download MP3', self)
        self.label.move(410, 125)
        self.label.setStyleSheet("color: solid black; font: 22pt")
        self.label.adjustSize()

        self.button = QPushButton('Convert', self)
        self.button.move(430, 290)
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(150)
        self.button.setStyleSheet("background: #A52A2A; color: white; border: 1px solid black; border-radius: 4px; font: 13pt")
        self.button.clicked.connect(self.clicked)
    
    def clicked(self):
        try:
            mp3_path = os.path.join(os.environ['USERPROFILE'], "Desktop")
            os.chdir(f'{mp3_path}')
            os.mkdir("MP3 Files")
            os.chdir(f'{mp3_path}\MP3 Files')
            
            new = self.link.text()
            video_info = YoutubeDL().extract_info(url=new, download=False)
            file = f"{video_info['title']}.mp3"

            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': file,
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

            YoutubeDL(options).download([video_info['webpage_url']])
        
        except FileExistsError:
            os.chdir(f'{mp3_path}\MP3 Files')
            new = self.link.text()
            
            video_info = YoutubeDL().extract_info(url=new, download=False)
            file = f"{video_info['title']}.mp3"

            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': file,
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

            YoutubeDL(options).download([video_info['webpage_url']])
            
def process():
    app = QApplication([])
    win1 = MP4()
    win2 = MP3()
    
    x = pg.prompt("Choose how you want to convert: (MP3/MP4)\n", "YouTube Converter").upper()
    if x == 'mp4'.upper():
        win1.show()
    elif x == 'mp3'.upper():
        win2.show()

    app.setStyle("Fusion")
    app.exec_()
process()
