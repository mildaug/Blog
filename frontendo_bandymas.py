import PySimpleGUI as sg

categories = [
    'Cars',
    'Home DIY',
    'Food',
    'Pets',
    'Hard drugs'
]

subtopics = {
    'Cars': ['BMW', 'Audi', 'Mercedes Benz'],
    'Home DIY': ['Gardening', 'Woodworking', 'Painting'],
    'Food': ['Italian', 'Asian', 'Fast Food'],
    'Pets': ['Dogs', 'Cats', 'Birds'],
    'Hard drugs': ['Cocaine', 'Heroin', 'Methamphetamine']
}

sg.theme('DarkAmber')
sg.set_options(font=('Courier New', 16))

category_layout = [
    [sg.Text('Category')],
    [sg.Combo(categories, size=(20, 1), key='CATEGORY_COMBO')],
    [sg.Button('Filter', key='FILTER_BUTTON')],
]

subtopic_layout = [
    [sg.Text('Posts')],

    [sg.Table(values=[], headings=['Posts', 'Upload date'], auto_size_columns=False, justification='left', size=(100, 6), col_widths=[30, 20], key='POST_TABLE', justification="left", enable_events=True)],
]

layout = [
    [
        sg.Column(category_layout),
        sg.Column(subtopic_layout),
    ],
    [sg.Button('Exit')],
]

window = sg.Window("Categories and Subtopics", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'CATEGORY_COMBO':
        selected_category = values['CATEGORY_COMBO']
        post_table = window['POST_TABLE']
        subtopic_list = subtopics.get(selected_category, [])
        post_table.update(values=[[subtopic] for subtopic in subtopic_list])

    if event == 'FILTER_BUTTON':
        selected_category = values['CATEGORY_COMBO']
        post_table = window['POST_TABLE']
        subtopic_list = subtopics.get(selected_category, [])
        post_table.update(values=[[subtopic] for subtopic in subtopic_list])

window.close()

