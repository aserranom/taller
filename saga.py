#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import wave
import audioop
import subprocess
from time import sleep


class InputType(object):
	
	def __init__(self):
		#os.system("sudo modprobe snd_bcm2835")
		print('Inicio')
	def next(self):
		pass# solo la enrada analga NO tiene que implementarlo

	def back(self):
		pass# solo la enrada analga NO tiene que implementarlo
		
	def can_play(self):
		raise Exception("can_play not implemented!")
	
	def pause(self):
		raise Exception('can not pause')

	def play(self):
		raise Exception("play not implemented!")

	def stop(self):
		raise Exception("play not implemented!")
	

class Test1(InputType):
	
	def __init__(self,x):
		self.x = x
		print(self.x)
		super(Test1, self).__init__()
		
	def next(self):
		print(self.x)
		print('next')

	def back(self):
		print(self.x)
		print('back')
		
	def can_play(self):
		
		return True
	
	def pause(self):
		print(self.x)
		print ('Pause')

	def play(self):
		print(self.x)
		print ('is plaing')

	def stop(self):
		print(self.x)
		print('stop')

class audio_local(InputType):
	
	def __init__(self):

		super(audio_local, self).__init__()
		
		
	def play(self):
		os.system("sudo mpc clear")
		os.system("sudo mpc update")
		os.system("sudo mpc add /")
		os.system("sudo mpc play")
		
	def stop(self):
		os.system("sudo mpc stop")

	def pause(self):
		os.system("sudo mpc pause")
			
	def can_play(self):
		pass
	#hay que verificar si hay por lo menos un archivo mp3
	#comando para que cambie de cancion
	
	def next(self):
		os.system("sudo mpc next")

	def back(self):
		os.system("sudo mpc prev")
	
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
	
		

class audio_analogo(InputType):
	'''
	Función que reproduce la entrada de audio analoga
	'''
	chunk = 1024
	
	def __init__(self):
	        """ Init audio stream """ 
	        self.p = pyaudio.PyAudio()
	        self.stream = self.p.open(
	            	format = pyaudio.paInt16,
	            	channels = 1,
	            	rate = 22000,
	            	input=True,
	            	output = True
	        )
	        self.reproduciendo = True
	
	def can_play(self):
	        try:
	            	"""
	            	mplayer_stream = subprocess.Popen(['mplayer', self.urls[0], '-dumpstream', '-dumpfile', 'out.dump'])
	            	sleep(2)
	            	mplayer_stream.terminate()
	            	mplayer_wav = subprocess.Popen(['mplayer', 'out.dump', '-ao', 'pcm:fast:file=dump.wav', '-af', 'format=s16le'])
	            	mplayer_wav.wait()
	            	"""
	            	#grabar un intervalo de audio en un archivo
	            	data = self.stream.read(self.chunk)
	            
	            	#wav_file = wave.open('basuraav', 'r')
	            	#data = wav_file.readframes(wav_file.getnframes())
	            	rms = audioop.rms(data, 2)
	            	#self.clean()
	            	if rms:
	                    	return True
	            	return False
	        except:
	            	return False
	
	def play(self):
	        """ Play entire file """
	        data = self.stream.read(self.chunk)
	        #while data != '' and reproduciendo:
	        while self.reproduciendo:
	            self.stream.write(data)
	            data = self.stream.read(self.chunk)
	
	def stop(self):
	        """ Graceful shutdown """
	        self.reproduciendo = False
	        self.stream.close()
	        self.p.terminate()

