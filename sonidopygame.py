from pygame import mixer
import pygame
import PySimpleGUI as sg
from threading import Thread
import os

class reproductor:
    def __init__(self):
        sg.theme('DarkGreen5')
        # Definimos los elementos de la interfaz grafica
        layout = [[sg.Button(button_text="Seleccionar Carpeta", key="carpeta"), sg.Button(button_text="Seleccionar Cancion", key="cancion")],
                  [sg.Image(filename='logo.png', key='-image-')],
                  [sg.Text(text="-------Nombre de la cancion----", key='name', justification=("center"))],
                  [sg.Button('Anterior'), sg.Button(button_text='Pausar', key="pausa"), sg.Button('Siguiente')]]
        # Creamos la interfaz grafica
        self.window = sg.Window('Reproductor',
                           layout,
                           no_titlebar=False,
                           location=(0, 0))
        self.boton_pausa = self.window['pausa']
        self.nombre_cancion = self.window['name']
        self.ruta = ""
        self.canciones = []
        self.estado = False
        self.posicion = 0
        self.pausa = False
        self.proceso = ""

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
