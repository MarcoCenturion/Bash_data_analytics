import PySimpleGUIQt as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout)
event, values = window.read()
window.close()

sg.Popup(event, values[0])
