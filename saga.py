#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
class InputType(object):
	
	def __init__(self):
		os.system("sudo modprobe snd_bcm2835")

	def next(self):
		pass# solo la enrada analga NO tiene que implementarlo
	
	def can_play(self):
		raise Exception("can_play not implemented!")

	def play(self):
		raise Exception("play not implemented!")

	def stop(self):
		raise Exception("play not implemented!")
	

class audio_local(InputType):
	
	def __init__(self):

		super(audio_local, self).__init__()
		
		
	def play(self):
		os.system("sudo mpc clear")
		os.system("sudo mpc update")
		os.system("sudo mpc add *.mp3")
		os.system("sudo mpc play")
		
	def stop(self):
		os.system("sudo mpc stop")
		
	def can_play(self):
		pass
	#hay que verificar si hay por lo menos un archivo mp3
	
	def play(self):
		pass
	#comando para que cambie de cancion
	
class audio_web(InputType):
	
	def __init__(self, urls = "http://65.60.34.34:8030" ):
		super(audio_web, self).__init__()
		self.urls = urls
		

	def next(self):
	    return InputType.next(self)


	def can_play(self):
	    return InputType.can_play(self)


	def play(self):
		os.system("sudo mpc clear")
		for url in self.urls:
			os.system("sudo mpc add echo " + url)
		os.system("sudo mpc play")

	def stop(self):
	    os.system("sudo mpc stop")

	
		
def audio_local():
	'''
	Función que reproduce un archivo mp3
	'''
	# Asegurarse de tener cargado el módulo de sonido
	os.system("sudo modprobe snd_bcm2835")
	# Borrar la lista anterior
	os.system("sudo mpc clear")
	# Agregar al playlist el archivo de audio
	# los archivos deben estar antes en  la carpeta /var/lib/mpd/music
	os.system("sudo mpc update")
	os.system("sudo mpc add *.mp3")
	# Se Reproduce el archivo
	os.system("sudo mpc play")#sudo
	# Se detiene la reproducción
	raw_input("Presione Enter para continuar...")
	os.system("sudo mpc stop")#sudo

def audio_analogo():
	'''
	Función que reproduce la entrada de audio analoga
	'''
	pass

def audio_web():
	'''
	Función que reproduce un stream de audio desde internet
	'''
	# Asegurarse de tener cargado el módulo de sonido
	os.system("sudo modprobe snd_bcm2835")
	# Url de entrada
	url = "http://65.60.34.34:8030"
	user_url = raw_input("Indica una URL o apreta enter para escuchar una por default: ")
	if user_url:
		url = user_url
	# Se agrega la Url a la lista de playlists de mpc
	os.system("sudo mpc add echo " + url)#sudo mpc add
	# Se toca la Url agregada
	os.system("sudo mpc play")#sudo
	# Se detiene la reproducción
	raw_input("Presione Enter para continuar...")
	os.system("sudo mpc stop")#sudo

