from Tkinter import *
import tkFont
class PlayList:
    def __init__(self, canciones=["lala", "boing", "mala", "c1", "c2", "c3","c4"]):
        self.list = canciones
    def songListBox(self, listBox):
        for song in self.list:
            listBox.insert(END,song)
