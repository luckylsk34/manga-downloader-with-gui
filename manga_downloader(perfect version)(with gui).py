#!/usr/bin/env python3

import os
import sys
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("Manga Downloader")
w.setGeometry(800, 400, 350, 200)

#manga name
manga_label = QLabel(w)
manga_label.setText("manga")
manga_label.move(96, 20)

manga_name = QLineEdit(w)
manga_name.setToolTip("enter the name of the manga")
manga_name.move(175, 15)

#starting chapter
starting_label = QLabel(w)
starting_label.setText("starting chapter")
starting_label.move(32, 60)

starting_chapter = QLineEdit(w)
starting_chapter.setToolTip("enter the starting chapter")
starting_chapter.move(175, 55)

#ending chapter
ending_label = QLabel(w)
ending_label.setText("ending chapter")
ending_label.move(39, 90)

ending_chapter = QLineEdit(w)
ending_chapter.setToolTip("enter the ending chapter")
ending_chapter.move(175, 85)

#submit button
submit = QPushButton("Submit", w)
submit.setToolTip("Submit the details")
submit.move(130, 140)

w.show()

def s_submit():
	os.system("gnome-terminal -e 'python3 download.py \"%s\" %d %d'"%(manga_name.text(), int(starting_chapter.text()), int(ending_chapter.text())))

submit.clicked.connect(s_submit)

sys.exit(app.exec_())
