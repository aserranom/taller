#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os

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

