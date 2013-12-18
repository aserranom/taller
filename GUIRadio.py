from Tkinter import *
from RadioInterface import *
ventana = Tk()
ventana.wm_title("SAGA 1 - Taller de Diseño")
playList = PlayList()
radioInterface = RadioInterface(ventana, playList)
ventana.mainloop()
