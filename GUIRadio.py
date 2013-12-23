#!/bin/sh
""":"
exec python $0 ${1+"$@"}
"""
from Tkinter import *
from RadioInterface import *
import thread
import audio_controler
from saga import *

    
    
if __name__ == "__main__":
    ventana = Tk()
    ventana.wm_title("SAGA 1 - Taller de Diseno")
    playList = PlayList()
    input_a = (audio_analogo(), audio_web(),audio_local())
    
    radioInterface = RadioInterface(ventana, playList)
    control = audio_controler.audio_controler( input_a )
    radioInterface.setControl(control)
    thread.start_new(control.start, ())

    ventana.mainloop()

    control.killme()
    
    
    #thread.start_new_thread(initInterface, ventana)
    
    
