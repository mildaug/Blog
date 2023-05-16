import PySimpleGUI as sg

layout = [
    [
        sg.Button('Cars', key='-CARS-'),
        sg.Button('Home DIY', key='-HOME_DIY-'),
        sg.Button('FOODS', key='-FOODS-'),
        sg.Button('Pets', key='-PETS-'),
        sg.Button('Hard Drugs', key='-HARD_DRUGS-')
    ],
    [
        sg.Button(button_color=('white', 'firebrick3'), button_text=('EXIT'), size=(20, 1), focus=True, key='Exit')
    ]
]

layout_cars = [
    [
        sg.Button('BMW'),
        sg.Button('Audi'),
        sg.Button('Mercedes Benz'),
    ]
]

window = sg.Window('Button Example', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == '-CARS-':
        cars_window = sg.Window('Cars', layout_cars)
        while True:
            event_cars, values_cars = cars_window.read()
            if event_cars == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the cars window
            elif event_cars == 'BMW':
                sg.popup('BMW Clicked!')
            elif event_cars == 'Audi':
                sg.popup('Audi Clicked!')
            elif event_cars == 'Mercedes Benz':
                sg.popup('Mercedes Benz Clicked!')
        cars_window.close()

    elif event == '-HOME_DIY-':
        sg.popup('Button Clicked!')

    elif event == '-FOODS-':
        sg.popup('Button Clicked!')

    elif event == '-PETS-':
        sg.popup('Button Clicked!')

    elif event == '-HARD_DRUGS-':
        sg.popup('Button Clicked!')

window.close()
