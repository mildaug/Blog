import PySimpleGUI as sg

main_layout = [
        [
        sg.Button('Topic1', key='-CARS-'),
        sg.Button('Topic2', key='-HOME_DIY-'), 
        sg.Button('Topic3', key='-FOODS-'),
        sg.Button('Topic4', key='-PETS-'),
        sg.Button('Topic5', key='-HARD_DRUGS-')
        ], 
        [sg.Button(button_color=('white', 'firebrick3'), button_text=('EXIT'), size=(40, 1), focus=True, key='Exit')]
]

popup_layout = [
        [
        sg.Button('button1', key='-A-'),
        sg.Button('button2', key='-B-'), 
        sg.Button('button3', key='-C-')
        ], 
        [sg.Button(button_color=('white', 'firebrick3'), button_text=('EXIT'), size=(20, 1), focus=True, key='Exit')]
]

main_window = sg.Window('Button Example', main_layout)
popup_window = sg.Window('Button Example', popup_layout)

while True:
    event, values = main_window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == '-CARS-':
        while True:
            event, values = popup_window.read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break

            elif event == '-A-':
                sg.popup('Button Clicked!')


    elif event == '-HOME_DIY-':
        sg.popup('Button Clicked!')

    elif event == '-FOODS-':
        sg.popup('Button Clicked!')

    elif event == '-PETS-':
        sg.popup('Button Clicked!')

    elif event == '-HARD_DRUGS-':
        sg.popup('Button Clicked!')

main_window.close()