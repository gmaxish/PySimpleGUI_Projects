import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['seconds to minutes' , 'meters to km'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_values = values['-INPUT-']
        if input_values.isnumeric():
            match values['-UNITS-']:
                case 'meters to km':
                    output = float(input_values) / 1000
                    output_string = f'{input_values} meters are {output} km.'
                case 'seconds to minutes':
                    minutes = round(int(input_values) / 60, 2)
                    output_string = f'{input_values} seconds = {minutes} minutes.'

            window['-OUTPUT-'].update(output_string)


window.close()