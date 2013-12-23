from Tkinter import *
from PlayList import *
import tkFont
import thread
import os

class RadioInterface:
    def __init__(self, ventana, playList):
        
        
        #self.control = control
        self.control=None
        
        ventana.minsize(650,360)
        ventana.maxsize(ventana.winfo_screenwidth(),ventana.winfo_screenheight())

       #carga de imagenes
        img_play        = PhotoImage(file="button_play.gif")
        img_pause       = PhotoImage(file="button_pause.gif")
        img_stop        = PhotoImage(file="button_stop.gif")
        img_back        = PhotoImage(file="button_backward.gif")
        img_forward     = PhotoImage(file="button_forward.gif")
        img_bg          = PhotoImage(file="bg.gif")

        #imagen background 
        self.button_bg          = Label(ventana, image=img_bg)
        self.button_bg.img_bg   = img_bg
        self.button_bg.place(x=0, y=0)
        
        #nombre de la aplicacion
        self.frame_NameApp = Frame(ventana, bg = "#f0f0f0")
        self.frame_NameApp.pack(side = TOP)

        self.label_NameApp = Label(self.frame_NameApp, font=("Helevtica",14), text = "Sistema automatizado para gestion de audio - SAGA v0.1.", anchor = E)
        self.label_NameApp.pack(side = TOP)

        #control de volumen
        self.frame_controlsVolume = Frame(ventana, width = 300, height = 80)
        self.frame_controlsVolume.pack_propagate(False)
        self.frame_controlsVolume.place(x=30, y=180)
        
        self.scale_volume = Scale(self.frame_controlsVolume, from_=0, to=100, width="30", length="100", orient=HORIZONTAL, command = self.volume)
        self.scale_volume.pack()
        self.label_volume = Label(self.frame_controlsVolume, font=("Helevtica",14), text = "Volumen", anchor = E)
        self.label_volume.pack(side = TOP)
        self.scale_volume.set(50)

        #controles de la radio |<< |> || [] >>|
        self.frame_controlsRadio = Frame(ventana, width = 500, height = 100)
        self.frame_controlsRadio.pack_propagate(False)
        self.frame_controlsRadio.place(x=30, y=60)
        self.label_cancion = Label(self.frame_controlsRadio,width = 100, font=("Helevtica",16), text = "nombre de cancion", bd = 2, bg = "white", anchor = W)
        self.label_cancion.pack(side = TOP)
        
        self.button_back            = Button(self.frame_controlsRadio, image=img_back,  command = self.back)
        self.button_back.img_back   = img_back
        self.button_back.pack(side  = LEFT)

        self.button_play            = Button(self.frame_controlsRadio, image=img_play,  command = self.play)
        self.button_play.img_play   = img_play
        self.button_play.pack(side  = LEFT)

        self.button_pause           = Button(self.frame_controlsRadio, image=img_pause, command = self.pause)
        self.button_pause.img_pause = img_pause
        self.button_pause.pack(side = LEFT)
        
        self.button_stop            = Button(self.frame_controlsRadio, image=img_stop,  command = self.stop)
        self.button_stop.img_stop   = img_stop
        self.button_stop.pack(side  = LEFT)
        
        self.button_forward         = Button(self.frame_controlsRadio, image=img_forward,command = self.forward)
        self.button_forward.img_forward= img_forward
        self.button_forward.pack(side = LEFT)

        #Playlist 
        ''' el playlist la tiene que implemetar la entrada de audio local,
         el play tiene que llamas al controlador'''
        '''self.frame_playlist = Frame(ventana, width = 300, height = 130)
        self.frame_playlist.pack_propagate(False)
        self.frame_playlist.place(x=250, y=200)

        self.label_playlist = Label(self.frame_playlist, font=("Helevtica",14), text = "Playlist - SD Card", anchor = E)
        self.label_playlist.pack(side = TOP)

        self.scrollbar = Scrollbar(self.frame_playlist, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.lista   = Listbox(self.frame_playlist, height=10, yscrollcommand = self.scrollbar.set)
        self.lista.pack(side = TOP, fill = BOTH)
        playList.songListBox(self.lista)

        self.scrollbar.configure(command=self.lista.yview)'''


        #Inputs
        self.frame_inputs = Frame(ventana, width = 200, height = 130)
        self.frame_inputs.pack_propagate(False)
        self.frame_inputs.place(x=250, y=180)
        self.label_inputs = Label(self.frame_inputs, font=("Helevtica",14), text = "Entrada", anchor = E)
        self.label_inputs.pack(side = TOP)

        self.label_input_1 = Label(self.frame_inputs, font=("Helevtica",14), text = "   Local", anchor = W)
        self.label_input_1.configure(borderwidth=5,relief=RIDGE)
        self.label_input_1.pack(side = TOP, fill=BOTH)
        self.label_input_1.configure(bg='gray')

        self.label_input_2 = Label(self.frame_inputs, font=("Helevtica",14), text = "   Internet", anchor = W)
        self.label_input_2.configure(borderwidth=5,relief=RIDGE)
        self.label_input_2.pack(side = TOP, fill=BOTH)
        self.label_input_2.configure(bg='gray')

        self.label_input_3 = Label(self.frame_inputs, font=("Helevtica",14), text = "   Analoga", anchor = W)
        self.label_input_3.configure(borderwidth=5,relief=RIDGE)
        self.label_input_3.pack(side = TOP, fill=BOTH)
        self.label_input_3.configure(bg='gray')

        '''#Outputs
        self.frame_outputs = Frame(ventana, width = 200, height = 100)
        self.frame_outputs.pack_propagate(False)
        self.frame_outputs.place(x=570, y=200)
        self.label_outputs = Label(self.frame_outputs, font=("Helevtica",14), text = "Salida", anchor = E)
        self.label_outputs.pack(side = TOP)

        self.label_output_1 = Label(self.frame_outputs, font=("Helevtica",14), text = "   Analoga", anchor = W)
        self.label_output_1.configure(borderwidth=5,relief=RIDGE)
        self.label_output_1.pack(side = TOP, fill=BOTH)
        self.label_output_1.configure(bg='gray')

        self.label_output_2 = Label(self.frame_outputs, font=("Helevtica",14), text = "   Internet", anchor = W)
        self.label_output_2.configure(borderwidth=5,relief=RIDGE)
        self.label_output_2.pack(side = TOP, fill=BOTH)
        self.label_output_2.configure(bg='gray')
	'''


    def back(self):
        self.control.back()
        self.label_cancion.config(text = "Previous Song")
        #self.setInputandOutput(3,1)

    def play(self):
        self.control.play()
        #self.label_cancion.config(text = "Playing Song")
        #index = self.lista.curselection()
        #print self.lista.get(int(index[0]))
        #self.label_cancion.config(text = self.lista.get(int(index[0])) )

    def pause(self):
        self.control.pause()
        self.label_cancion.config(text = "Paused Song")

    def stop(self):
        self.control.stop()
        self.label_cancion.config(text = "Stopped Song")

    def forward(self):
        self.control.forward()
        self.label_cancion.config(text = "Next Song")
        #self.setInputandOutput(1,2)

    def volume(self,num):
        self.label_cancion.config(text = num)
	os.system('amixer set Speaker '+ str(num)+'%')

    def setInputandOutput(self, entrada, salida):

        if salida==1:
            self.label_output_1.configure(bg='yellow')
            self.label_output_2.configure(bg='gray')

        if salida==2:
            self.label_output_1.configure(bg='gray')
            self.label_output_2.configure(bg='yellow')

        if entrada==1:
            self.label_input_1.configure(bg='yellow')
            self.label_input_2.configure(bg='gray')
            self.label_input_3.configure(bg='gray')

        if entrada==2:
            self.label_input_1.configure(bg='gray')
            self.label_input_2.configure(bg='yellow')
            self.label_input_3.configure(bg='gray')

        if entrada==3:
            self.label_input_1.configure(bg='gray')
            self.label_input_2.configure(bg='gray')
            self.label_input_3.configure(bg='yellow')
    
    def setControl(self, newControl):
    	self.control=newControl
    	
    def setInterfaceInput(self, entrada):
    	if entrada == 0:#local 0
    	    self.label_input_1.configure(bg='yellow')
    	    self.label_input_2.configure(bg='gray')
    	    self.label_input_3.configure(bg='gray')
    	if entrada == 2:#analogo 2
    	    self.label_input_1.configure(bg='gray')
    	    self.label_input_2.configure(bg='yellow')
    	    self.label_input_3.configure(bg='gray')
    	if entrada == 1:#web 1
    	    self.label_input_1.configure(bg='gray')
    	    self.label_input_2.configure(bg='gray')
    	    self.label_input_3.configure(bg='yellow')
