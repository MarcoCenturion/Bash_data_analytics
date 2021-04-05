import PySimpleGUIQt as gui

gui.theme('Tan')
layout = [
    [gui.Text('hello')],
    [gui.Button('Ok')]
    ]


window = gui.Window('My window', layout)
event, vals = window.read()
window.close()
