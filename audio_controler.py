import saga
import thread
import os
from audio_controler import *
import time


class audio_controler:

	def __init__(self,input_):
		
		self.funciones = []	
		for inpt in input_:
			self.funciones.append(inpt)
		self.reproducir = 0
		self.isPause = False
		self.keepgoing = True
		#os.system("echo " + passwrd + " | sudo -S echo 'its on'")

	def back(self):
		self.funciones[self.reproducir].back()
	
	def play(self):
		self.isPause = False
		self.funciones[self.reproducir].play()
	
	def pause(self):
		self.isPause = True
		self.funciones[self.reproducir].pause()
	
	def stop(self):
		self.funciones[self.reproducir].stop()
	
	def forward(self):
		self.funciones[self.reproducir].next()

	def killme(self):
		self.funciones[self.reproducir].stop()
		self.keepgoing = False 
	
	
	def start(self):
		'''indica cual es la entrada con la que va a inicia la reproduccion'''
		
		cont = 0
		begin_thread = True

		while 1 and self.keepgoing:				
			
			time.sleep(0.5)
			if self.isPause:
				continue
		
			if begin_thread:
				thread.start_new_thread( self.funciones[self.reproducir].play,())
				begin_thread = False
			if self.reproducir > 0:
				for i in range(self.reproducir):
					if self.funciones[i].can_play():
						self.funciones[self.reproducir].stop()
						self.reproducir = i
						begin_thread = True
		
						break
			time.sleep(0.5)
			print '\n\n'+'-'*10+'inicio\n',self.funciones[self.reproducir].can_play(),self.funciones[self.reproducir]
			print '\n\n'+'-'*10+'fin\n'
			if not self.funciones[self.reproducir].can_play():
				
				self.funciones[self.reproducir].stop()
				# es para combiar la entrada si no esta reproduciendo
				if self.reproducir < len(self.funciones)-1:
					begin_thread = True
					self.reproducir += 1
				elif len(self.funciones)-1 == self.reproducir:
					raise Exception("Nothing to play")
					
				

			
			
						
			
	

