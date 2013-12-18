from Tkinter import *
from RadioInterface import *
import thread
import audio_controler
from saga import *
    
    
    
if __name__ == "__main__":
    ventana = Tk()
    ventana.wm_title("SAGA 1 - Taller de Diseno")
    playList = PlayList()
    #input_ = 
    control = audio_controler.audio_controler( (Test1(1),Test1(2)) )
    radioInterface = RadioInterface(ventana, playList,control)
    thread.start_new(control.start, ())
    print('lol')
    ventana.mainloop()
    
    
    #thread.start_new_thread(initInterface, ventana)
    
    
