#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os

def audio_local():
	'''
	Función que reproduce un archivo mp3
	'''
	pass

def audio_analogo():
	'''
	Función que reproduce la entrada de audio analoga
	'''
	pass

def audio_web():
	'''
	Función que reproduce un stream de audio desde internet
	'''
	os.system("sudo modprobe snd_bcm2835")
	url = "http://65.60.34.34:8030"
	user_url = raw_input("Indica una URL o apreta enter para escuchar una por default: ")
	if user_url:
		url = user_url
	os.system("sudo mpc add " + url)
	os.system("sudo mpc play")
