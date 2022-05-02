import PySimpleGUI as sg
from pathlib import Path
smiles = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]
smile_event = smiles[1] + smiles[3] + smiles[5]

menu_layout = [
    ['File', ['Open', 'Save', '----', 'Exit']],
    ['Tools',['Word count']],
    ['Add', smiles]
]
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-')],
    [sg.Multiline(size=(40, 20), no_scrollbar=True, key='-TEXTBOX-')]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Word count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_cout = len(clean_text)
        char_count = (len(''.join(clean_text)))
        sg.popup(f'There are {word_cout} words and characters are {char_count}')

    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Save':
        file_path = sg.popup_get_file('Save', no_window=True, save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event in smile_event:
        current_text = values['-TEXTBOX-']
        new_text = current_text + ' ' + event
        window['-TEXTBOX-'].update(new_text)

window.close()