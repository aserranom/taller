#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import wave
import audioop
import subprocess
import signal
from time import sleep
import glob

class InputType(object):
	
	def __init__(self):
		os.system("sudo modprobe snd_bcm2835")
		
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
		print(self.x, 'Iniciar')
		super(Test1, self).__init__()
		self.plays = True
		
	def next(self):
		print(self.x)
		print('next')

	def back(self):
		print(self.x)
		print('back')
		
	def can_play(self):
		
		return self.plays
	
	def pause(self):
		print(self.x)
		print ('Pause')

	def play(self):
		
		print(self.x)
		print ('is plaing')

	def stop(self):
		print(self.x)
		print('stop')
		self.plays = False

class audio_local(InputType):
	
	def __init__(self):

		super(audio_local, self).__init__()
		thisDirec = '/home/pi/taller'
		os.chdir('/home/pi')
		self.playlist = glob.glob('*.mp3')
		os.chdir(thisDirec)
		print self.playlist
		
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
		return True
	#hay que verificar si hay por lo menos un archivo mp3
	#comando para que cambie de cancion
	
	def next(self):
		os.system("sudo mpc next")

	def back(self):
		os.system("sudo mpc prev")
	
class audio_web(InputType):
	
	def __init__(self, urls = ["http://85.17.30.132:9530"] ):
		super(audio_web, self).__init__()
		self.urls = urls
		self.stream = None

	def next(self):
		urls.rotate(-1)
		if self.can_play():
			self.stop()
			self.play()

	def back(self):
		urls.rotate(1)
		if self.can_play():
			self.stop()
			self.play()

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
			self.clean('out.dump')
			self.clean('dump.wav')
			if rms:
				return True
			print ''' FALSE THIS

'''
			return False
		except:
			print ''' FALSE THIS

'''
			return False

	def play(self):
		if not self.stream:
			self.stream = subprocess.Popen(['mpg321','-a', 'hw:1', self.urls[0]])

	def stop(self):
		if self.stream:
			self.stream.terminate()
			self.stream = None

	def clean(self,x):
		try:
			os.remove(x)
		except:
			pass
	
		

class audio_analogo(InputType):
	'''
	Objeto audio analogo que reproduce la entrada de audio analoga
	'''	
	def __init__(self):
		""" Init audio stream """ 
		self.stream = None
		self.toggle = True
		os.system('export AUDIODEV=hw:1,0')
		os.system('export AUDIODRIVER=alsa')
	
	def can_play(self):
		if 1:
			wav = subprocess.Popen('rec analog.wav trim 0 0:01', shell=True)
			wav.wait()
			wav_file = wave.open('analog.wav', 'r')
			data = wav_file.readframes(wav_file.getnframes())
			rms = audioop.rms(data, 2)
			#os.remove('analog.wav')
			if rms > 2500:
				return True
			return False
		if 0:
			return False
	
		return self.toggle

	def play(self):
		print 'lol'
		if not self.stream:
			self.stream = subprocess.Popen('arecord -D plughw:1 -f dat | aplay -D plughw:1', shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

	def pause(self):
		self.toggle = False
	
	def stop(self):
		if self.stream:
			os.killpg(self.stream.pid, signal.SIGTERM)
			self.stream = None

if __name__ == "__main__":
	a = audio_local()
	a.play()
	raw_input()
	print a.can_play()
	a.stop()

