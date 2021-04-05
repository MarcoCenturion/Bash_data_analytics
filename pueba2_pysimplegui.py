import PySimpleGUIQt as sg


sg.theme('Reddit')

layout = [[sg.Text('Membresias',size=(40,1),key='-OUTPUT-')],
		 [sg.Text('BLUE',size=(40,1),key='-BLUE-')],
		 [sg.Text("Definir el costo USD por día")],
		 [sg.Spin([i for i in range(33,55)], initial_value=38), sg.Text('Valor noche USD')],
#		 	[sg.Slider(range=(50,33), orientation='h',font=('Atial', 12),size=(10,13), default_value=35),],
#		 [sg.Checkbox2('Un año', True),sg.Checkbox('Tres años'),sg.Checkbox('Cinco años')],
#		 [sg.InputOptionMenu(('Un año', 'Tres años', 'Cinco años'))],
		 [sg.Listbox(values=('Un año', 'Tres años', 'Cinco años'), size=(15, 4)),],
		 [sg.Button('Calcular'), sg.Button('Salir')]
		 ]

window = sg.Window('Membresias',layout)

while True:
	event, values = window.read(timeout=300)
	if event == sg.WINDOW_CLOSED or event == 'Salir':
		break 

	if event == 'Calcular':
		print()

	#window['-OUTPUT-'].update('Hola' * values['-INPUT-'])

window.close()