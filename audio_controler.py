import saga
import thread
import os



class audio_controler:

	def __init__(self,passwrd = "",input_):
		
		self.funciones = []	
		for inpt in input_:
			self.funciones.append(inpt)
		print self.funciones
		#os.system("echo " + passwrd + " | sudo -S echo 'its on'")

	def start(self):
		'''indica cual es la entrada con la que va a inicia la reproduccion'''
		reproducir = 2
		cont = 0
		begin_thread = True
		'''Esto es para testar el codifo'''
		print self.funciones[0].can_play(),self.funciones[1].can_play(),self.funciones[2].can_play()
		'''hasta aca'''
		while 1 and True:	
			

		
			if begin_thread:
				thread.start_new_thread( self.funciones[reproducir].play,())
				begin_thread = False
			if reproducir > 0:
				for i in range(reproducir):
					if self.funciones[i].can_play():
						self.funciones[reproducir].stop()
						reproducir = i
						begin_thread = True
		
						break
			if not self.funciones[reproducir].can_play():
				self.funciones[reproducir].stop()# es para combiar la entrada si no esta reproduciendo
				if reproducir < len(self.funciones)-1:
					begin_thread = True
					reproducir += 1
				elif len(self.funciones)-1 == reproducir:
					raise Exception("Nothing to play")
					
				

			
			
						
			
	

