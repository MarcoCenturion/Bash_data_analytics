import PySimpleGUIQt as sg
from pygame import mixer
import pygame
from threading import Thread
import os

def reproducir(self, ruta):
    self.estado = True
    try:
 
        mixer.init()
        mixer.music.load(ruta)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        while True:
            if self.estado == False:
                break
            elif self.proceso == "pausa":
                mixer.music.pause()
                self.proceso = ""
            elif self.proceso == "continuar":
                mixer.music.unpause()
                self.proceso = ""
 
    except pygame.error:
        pass

def cargar_cancion(self, ruta,cancion):
    hilo = Thread(target=self.reproducir, args=(ruta + "/" + cancion, ), daemon= True)
    hilo.start()

def cargar_cancion_unica(self, ruta):
    hilo2 = Thread(target=self.reproducir, args=(ruta,), daemon= True)
    hilo2.start()

def iniciar(self):
    while True:
        # Obtenemos informacion de la interfaz grafica y video
        event, values = self.window.read(timeout=100)
 		
 		if event == "carpeta":
            self.canciones = []
            self.ruta = ""
 	        self.estado = False
     	    self.ruta = sg.popup_get_folder(title='Seleccionar Carpeta', message="Carpeta")
            for archivo in os.listdir(self.ruta):
            	if archivo.endswith(".mp3"):
                    self.canciones.append(archivo)
            print(self.canciones)
            print(self.ruta)
            if len(self.canciones) == 0:
                pass
            else:
                self.nombre_cancion.update(self.canciones[0])
                self.cargar_cancion(self.ruta, self.canciones[0])