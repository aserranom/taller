from Tkinter import *
class RadioInterface:
    def __init__(self, ventana):

        ventana.minsize(600,400)
        
        #nombre de la aplicacion
        self.frame_NameApp = Frame(ventana, bg = "blue")
        self.frame_NameApp.pack(side = TOP)
        
        self.label_NameApp = Label(self.frame_NameApp, text = "SAGA 1", anchor = E)
        self.label_NameApp.pack(side = TOP)

        #controles de la radio |<< |> || >>|
        self.frame_controlsRadio = Frame(ventana, width = 200, height = 40)
        self.frame_controlsRadio.pack_propagate(False)
        self.frame_controlsRadio.pack(side = TOP)
        self.label_cancion = Label(self.frame_controlsRadio,width = 100,text = "   walala   ", bd = 2, bg = "white")
        self.label_cancion.pack(side = TOP)
        
        self.button_back = Button(self.frame_controlsRadio, text = "|<<", command = self.back)
        self.button_back.pack(side = LEFT)
        self.button_play = Button(self.frame_controlsRadio, text = "||", command = self.play)
        self.button_play.pack(side = LEFT)
        self.button_pause = Button(self.frame_controlsRadio, text = "|>", command = self.pause)
        self.button_pause.pack(side = LEFT)
        self.button_forward = Button(self.frame_controlsRadio, text = ">>|", command = self.forward)
        self.button_forward.pack(side = LEFT)

    def back(self):
        self.label_cancion.config(text = "back")

    def play(self):
        self.label_cancion.config(text = "play")

    def pause(self):
        self.label_cancion.config(text = "pause")

    def forward(self):
        self.label_cancion.config(text = "forward")
