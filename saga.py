#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import wave
import audioop
import subprocess
from time import sleep


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
	
	def __init__(self, urls = ["http://65.60.34.34:8030"] ):
		super(audio_web, self).__init__()
		self.urls = urls
		self.stream = None

	def next(self):
		urls.rotate(-1)
		if self.can_play():
			self.play()
		else:
			return False

	def can_play(self):
		try:
			mplayer_stream = subprocess.Popen(['mplayer', self.urls[0], '-dumpstream', '-dumpfile', 'out.dump'])
			sleep(2)
			mplayer_stream.terminate()
			mplayer_wav = subprocess.Popen(['mplayer', 'out.dump', '-ao', 'pcm:fast:file=dump.wav', '-af', 'format=s16le'])
			mplayer_wav.wait()
			wav_file = wave.open('dump.wav', 'r')
			data = wav_file.readframes(wav_file.getnframes())
			rms = audioop.rms(data, 2)
			self.clean()
			if rms:
				return True
			return False
		except:
			return False

	def play(self):
		new_stream = subprocess.Popen(['mplayer', self.urls[0]])
		self.stop()
		self.stream = new_stream

	def stop(self):
		if self.stream:
			self.stream.terminate()
			self.stream = None

	def clean(self):
		os.remove('out.dump')
		os.remove('dump.wav')
	
		
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
'''
def audio_web():
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
'''
