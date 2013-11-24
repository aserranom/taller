import saga
import thread
import os

class BigInput(object):
	def __init__(self,x):
		self.canDo= True
		self.numerode = str(x)

	def can_play(self):
		return self.canDo

	def restar(self):
		os.system("sudo echo 'Buffer reproduciendo "+self.numerode+"'")
		self.canDo= True

	def play(self):
		while self.canDo:
			os.system("sudo echo 'Esta reproduciendo "+self.numerode+"'")

	def stop(self):
		os.system("sudo echo 'Esta reproduciendo se paro "+self.numerode+"'")
		self.canDo = False

class input1(BigInput):
	def __init__(self):
		super(input1, self).__init__(1)

class input2(BigInput):
	def __init__(self):
		super(input2, self).__init__(2)
		
class input3(BigInput):
	def __init__(self):
		super(input3, self).__init__(3)

class audio_controler:

	def __init__(self,passwrd = "",input_):
		
		self.funciones = []	
		for inpt in input_:
			self.funciones.append(inpt)
		
		#self.funciones.append(saga.audio_local)
		#self.funciones.append(saga.audio_analogo)
		#self.funciones.append(saga.audio_web)
		print self.funciones
		
		os.system("echo " + passwrd + " | sudo -S echo 'its on'")

	def start(self):
		'''indica cual es la entrada con la que va a inicia la reproduccion'''
		reproducir = 2
		cont = 0
		begin_thread = True
		'''Esto es para testar el codifo'''
		gap = 1000000
		print self.funciones[0].can_play(),self.funciones[1].can_play(),self.funciones[2].can_play()
		'''hasta aca'''
		while 1 and True:	
			

			cont += 1#parte del testeo
			if begin_thread:
				thread.start_new_thread( self.funciones[reproducir].play,())
				begin_thread = False
			if reproducir > 0:
				for i in range(reproducir):
					#print i
					if self.funciones[i].can_play():
						self.funciones[reproducir].stop()
						reproducir = i
						begin_thread = True
						print self.funciones[0].can_play(),self.funciones[1].can_play(),self.funciones[2].can_play() #test
						break
			if not self.funciones[reproducir].can_play():
				self.funciones[reproducir].stop()# es para combiar la entrada si no esta reproduciendo
				if reproducir < len(self.funciones)-1:
					begin_thread = True
					reproducir += 1
				elif len(self.funciones)-1 == reproducir:
					raise Exception("Nothing to play")
					
				
			####################################el resto es para test
			
			if cont == gap:
				print cont
				self.funciones[reproducir].stop()
			elif cont == 2*gap:
				print cont
				self.funciones[reproducir].stop()
			elif cont == 4*gap:
				self.funciones[1].restar()
			elif cont == 6*gap:
				self.funciones[0].restar()
			
			
						
			
			

aux = audio_controler("")
aux.start()

