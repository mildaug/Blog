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

likes = {
    'Cars': {'BMW': 0, 'Audi': 0, 'Mercedes Benz': 0},
    'Home DIY': {'Gardening': 0, 'Woodworking': 0, 'Painting': 0},
    'Food': {'Italian': 0, 'Asian': 0, 'Fast Food': 0},
    'Pets': {'Dogs': 0, 'Cats': 0, 'Birds': 0},
    'Hard drugs': {'Cocaine': 0, 'Heroin': 0, 'Methamphetamine': 0}
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
    [
        sg.Table(
            values=[],
            headings=['Posts', 'Likes'],
            auto_size_columns=False,
            size=(100, 6),
            col_widths=[30, 10],
            key='POST_TABLE',
            justification='left',
            enable_events=True,
            select_mode=sg.TABLE_SELECT_MODE_BROWSE
        )
    ],
]

button_layout = [
    [sg.Button('Add Category', key='ADD_CATEGORY_BUTTON')],
    [sg.Button('Add Post', key='ADD_POST_BUTTON')],
    [sg.Button('Like', key='LIKE_BUTTON')],
]

layout = [
    [
        sg.Column(category_layout),
        sg.Column(subtopic_layout),
        sg.Column(button_layout),
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
        post_table.update(values=[[subtopic, likes[selected_category].get(subtopic, 0)] for subtopic in subtopic_list])

    if event == 'FILTER_BUTTON':
        selected_category = values['CATEGORY_COMBO']
        post_table = window['POST_TABLE']
        subtopic_list = subtopics.get(selected_category, [])
        post_table.update(values=[[subtopic, likes[selected_category].get(subtopic, 0)] for subtopic in subtopic_list])

    if event == 'ADD_CATEGORY_BUTTON':
        new_category = sg.popup_get_text('Enter new category:')
        if new_category:
            categories.append(new_category)
            subtopics[new_category] = []
            likes[new_category] = {}
            window['CATEGORY_COMBO'].update(values=categories)

    if event == 'ADD_POST_BUTTON':
        selected_category = values['CATEGORY_COMBO']
        new_post = sg.popup_get_text('Enter new post:')
        if new_post:
            subtopics[selected_category].append(new_post)
            likes[selected_category][new_post] = 0
            post_table = window['POST_TABLE']
            post_table.update(values=[[subtopic, likes[selected_category].get(subtopic, 0)] for subtopic in subtopics[selected_category]])

    if event == 'LIKE_BUTTON':
        selected_category = values['CATEGORY_COMBO']
        selected_row = values['POST_TABLE']
        if selected_row:
            selected_row = selected_row[0]
            selected_subtopic = subtopics.get(selected_category, [])[selected_row]
            likes[selected_category][selected_subtopic] += 1
            post_table = window['POST_TABLE']
            post_table.update(values=[[subtopic, likes[selected_category].get(subtopic, 0)] for subtopic in subtopics[selected_category]])

window.close()
