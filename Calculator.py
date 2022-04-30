import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='franklin 40')
    button_size = (3,1)
    layout = [
        [sg.Text('',
                 key='-OUTPUT-',
                 font='franklin 32',
                 justification='right',
                 expand_x=True,
                 pad=(10, 30),
                 right_click_menu=theme_menu)],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button('*', size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button('/', size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button('-', size=button_size)],
        [sg.Button(0, expand_x=True), sg.Button('.', size=button_size), sg.Button('+', size=button_size)]
    ]
    return sg.Window("Calculator", layout)

theme_menu =['menu', ['LightGrey1', 'dark', 'DarkGrey8', 'random']]
window = create_window('dark')

current_num = []
operators =[]

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-OUTPUT-'].update(num_string)

    if event in ['*', '/', '-', '+']:
        operators.append(''.join(current_num))
        current_num = []
        operators.append(event)
        window['-OUTPUT-'].update('')

    if event == 'Enter':
        operators.append(''.join(current_num))
        result = eval(''.join(operators))
        window['-OUTPUT-'].update(result)
        operators = []

    if event == 'Clear':
        operators =[]
        current_num = []
        window['-OUTPUT-'].update('')

window.close()