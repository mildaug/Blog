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

topic_layout = [
    [sg.Text('Topics')],
    [sg.Combo(categories, size=(20, 1), key='TOPIC_COMBO')],
    [sg.Button('Filter', key='FILTER_BUTTON')],
    [sg.Button('Add Topic', key='ADD_TOPIC_BUTTON')]
]

subtopic_layout = [
    [sg.Text('Posts')],
    [
        sg.Table(
            values=[],
            headings=['Posts', 'Upload date'],
            auto_size_columns=False,
            size=(100, 6),
            col_widths=[30, 20],
            key='POST_TABLE',
            justification='left',
            enable_events=True
        ),
    ],
]

button_layout = [
    [sg.Button('Add Post', key='ADD_POST_BUTTON')],
]

layout = [
    [
        sg.Column(topic_layout),
        sg.Column(subtopic_layout),
        sg.Column(button_layout),
    ],
    [sg.Button('Exit')],
]

window = sg.Window("Topics and posts", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'TOPIC_COMBO':
        selected_category = values['TOPIC_COMBO']
        post_table = window['POST_TABLE']
        subtopic_list = subtopics.get(selected_category, [])
        post_table.update(values=[[subtopic] for subtopic in subtopic_list])

    if event == 'FILTER_BUTTON':
        selected_category = values['TOPIC_COMBO']
        post_table = window['POST_TABLE']
        subtopic_list = subtopics.get(selected_category, [])
        post_table.update(values=[[subtopic] for subtopic in subtopic_list])

    if event == 'ADD_TOPIC_BUTTON':
        new_category = sg.popup_get_text('Enter new Topic:')
        if new_category:
            categories.append(new_category)
            subtopics[new_category] = []
            window['TOPIC_COMBO'].update(values=categories)

    if event == 'ADD_POST_BUTTON':
        selected_category = values['TOPIC_COMBO']
        new_post = sg.popup_get_text('Enter new post:')
        if new_post:
            subtopics[selected_category].append(new_post)
            post_table = window['POST_TABLE']
            post_table.update(values=[[subtopic] for subtopic in subtopics[selected_category]])

window.close()