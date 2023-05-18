import PySimpleGUI as sg

layout = [
    [
        sg.Button('Cars', key='-CARS-'),
        sg.Button('Home DIY', key='-HOME_DIY-'),
        sg.Button('Foods', key='-FOODS-'),
        sg.Button('Pets', key='-PETS-'),
        sg.Button('Hard drugs', key='-HARD_DRUGS-')
    ],
    [
        sg.Button(button_color=('white', 'firebrick3'), button_text=('EXIT'), size=(20, 1), focus=True, key='Exit')
    ]
]

def cars():
    layout_cars = [
        [
            sg.Button('BMW'),
            sg.Button('Audi'),
            sg.Button('Mercedes Benz'),
        ]
    ]
    return layout_cars

def home_diy():
    layout_home_diy = [
        [
            sg.Button('Gardening'),
            sg.Button('Woodworking'),
            sg.Button('Painting'),
        ]
    ]
    return layout_home_diy

def foods():
    layout_foods = [
        [
            sg.Button('Italian'),
            sg.Button('Asian'),
            sg.Button('Fast Food'),
        ]
    ]
    return layout_foods

def pets():
    layout_pets = [
        [
            sg.Button('Dogs'),
            sg.Button('Cats'),
            sg.Button('Birds'),
        ]
    ]
    return layout_pets

def hard_drugs():
    layout_hard_drugs = [
        [
            sg.Button('Cocaine'),
            sg.Button('Heroin'),
            sg.Button('Methamphetamine'),
        ]
    ]
    return layout_hard_drugs

window = sg.Window('Button Example', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == '-CARS-':
        cars_window = sg.Window('Cars', cars())
        while True:
            event_cars, values_cars = cars_window.read()
            if event_cars == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the cars window
            sg.popup(f'{event_cars} Clicked!')
        cars_window.close()

    elif event == '-HOME_DIY-':
        home_diy_window = sg.Window('Home DIY', home_diy())
        while True:
            event_home_diy, values_home_diy = home_diy_window.read()
            if event_home_diy == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the home DIY window
            sg.popup(f'{event_home_diy} Clicked!')
        home_diy_window.close()

    elif event == '-FOODS-':
        foods_window = sg.Window('Foods', foods())
        while True:
            event_foods, values_foods = foods_window.read()
            if event_foods == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the foods window
            sg.popup(f'{event_foods} Clicked!')
        foods_window.close()

    elif event == '-PETS-':
        pets_window = sg.Window('Pets', pets())
        while True:
            event_pets, values_pets = pets_window.read()
            if event_pets == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the pets window
            sg.popup(f'{event_pets} Clicked!')
        pets_window.close()

    elif event == '-HARD_DRUGS-':
        hard_drugs_window = sg.Window('Hard Drugs', hard_drugs())
        while True:
            event_hard_drugs, values_hard_drugs = hard_drugs_window.read()
            if event_hard_drugs == sg.WINDOW_CLOSED:
                break
            # Handle button clicks within the hard drugs window
            sg.popup(f'{event_hard_drugs} Clickedd!')
        hard_drugs_window.close()
           

