import PySimpleGUI as sg
from collections import defaultdict
from blog_backend import view_topic, get_users, view_posts, post_topic_join_by_topicname, add_topic, add_posts, Posts, session, engine
from datetime import datetime

all_topics = view_topic()
topics = [topics.topic_name for topics in all_topics]

all_posts = view_posts()
posts = [post.post_name for post in all_posts]

all_users = get_users()
user = [[user.id, user.user_name] for user in all_users]

likes = defaultdict(dict) # likes sudeda i nested dictionary

sg.theme('DarkAmber')
sg.set_options(font=('Courier New', 16))

topic_layout = [
            [sg.Text('Topic')],
            [sg.Combo(topics, size=(20, 1), key='TOPIC_COMBO')],
            [sg.Button('Filter', key='FILTER_BUTTON')],
        ]

post_layout = [
    [sg.Text('Posts')],
    [
        sg.Table(
            values=[],
            headings=['Posts', 'Date', 'Likes'],
            auto_size_columns=False,
            size=(100, 6),
            col_widths=[30, 11, 10],
            key='POST_TABLE',
            justification='left',
            enable_events=True,
            select_mode=sg.TABLE_SELECT_MODE_BROWSE
        )
    ],
]

def add_post_layout():
    add_post_layout = [
        [sg.Text('Enter post details:')],
        [sg.Text('Username:'), sg.Combo(user, key='user_name')],
        [sg.Text('Post Name:'), sg.Input(key='post_name')],
        [sg.Text('Content:'), sg.Input(key='content')],
        [sg.Text('Topic:'), sg.Combo(topics, key='topic_combo')],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]   
    return add_post_layout

button_layout = [
    [sg.Button('Add Topic', key='ADD_TOPIC_BUTTON')],
    [sg.Button('Add Post', key='ADD_POST_BUTTON')],
    [sg.Button('Like', key='LIKE_BUTTON')],
]

layout = [
    [
        sg.Column(topic_layout),
        sg.Column(post_layout),
        sg.Column(button_layout),
    ],
    [sg.Button('Exit')],
]


window = sg.Window("Topics and Posts", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'TOPIC_COMBO':
        selected_topic = values['TOPIC_COMBO']
        post_table = window['POST_TABLE']
        post_list = posts
        post_table.update(values=[[post, likes[selected_topic].get(post, 0)] for post in post_list])

    if event == 'FILTER_BUTTON':
        selected_topic = values['TOPIC_COMBO']
        post_table = window['POST_TABLE']
        all_posts = post_topic_join_by_topicname(selected_topic)
        selected_posts = []
        for post, topic in all_posts:
            selected_post = [post.post_name, post.date]
            selected_posts.append(selected_post)
        post_table.update(values=selected_posts)

    if event == 'ADD_TOPIC_BUTTON':
        new_topic = sg.popup_get_text('Enter new topic:')
        if new_topic:
            add_topic(new_topic)
            topics.append(new_topic)
            window['TOPIC_COMBO'].update(values=topics)

    if event == 'ADD_POST_BUTTON':
        layout = add_post_layout()
        add_post_window = sg.Window('Add Post', layout)
        while True:
            event, values = add_post_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Cancel":
                add_post_window.close()
            elif event == 'OK':
                new_post_username = values['user_name']
                new_post_id = new_post_username[0]
                new_post_name = values['post_name']
                new_post_content = values['content']
                new_post_date = datetime.now().strftime("%Y-%m-%d")
                selected_topic = values['topic_combo']
                topic_id = next(topic.id for topic in all_topics if topic.topic_name == selected_topic)
                new_post = add_posts(new_post_id, new_post_name, new_post_content, new_post_date, topic_id)
                add_post_window.close()


    if event == 'LIKE_BUTTON':
        selected_topic = values['TOPIC_COMBO']
        selected_row = values['POST_TABLE']
        if selected_row:
            selected_row = selected_row[0]
            selected_post = posts.get(selected_topic, [])[selected_row]
            likes[selected_topic][selected_post] += 1
            post_table = window['POST_TABLE']
            post_table.update(values=[[post, likes[selected_topic].get(post, 0)] for post in posts[selected_topic]])

window.close()
