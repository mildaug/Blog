from blog_backend import Posts, Likes, Topics, Users
from config import session, sg

topics = session.query(Topics).all()
users = session.query(Users).all()

topics_layout = [
    [sg.Text('User')],
    [sg.Combo(users, size=(20, 1), key='USER_COMBO', enable_events=True)],
    [sg.Text('Topic')],
    [sg.Combo(topics, size=(20, 1), key='TOPIC_COMBO', enable_events=True)],
]

posts_layout = [
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

buttons_layout = [
    [sg.Button('View Post', key='VIEW_POST_BUTTON', disabled=True)],
    [sg.Button('Like', key='LIKE_BUTTON', disabled=True)],
    [sg.Button('Add Topic', key='ADD_TOPIC_BUTTON')],
    [sg.Button('Add Post', key='ADD_POST_BUTTON', disabled=True)],
    [sg.Button('Edit Post', key='EDIT_POST_BUTTON', disabled=True)],
]

main_layout = [
    [
        sg.Column(topics_layout),
        sg.Column(posts_layout),
        sg.Column(buttons_layout),
    ],
    [sg.Button('Exit')],
]

def view_post_layout(post: Posts):
    layout = [
        [sg.Text(post.name)],
        [sg.Multiline(post.content, size=(50, 10), key='POST_CONTENT', disabled=True)],
        [sg.Button('Close'), sg.Button('Comment', key='COMMENT'), sg.Button('Like', key='LIKE_BUTTON')],
    ]
    return layout

def add_post_layout():
    add_post_layout = [
        [sg.Text('Enter post details:')],
        [sg.Text('Title:'), sg.Input(key='POST_NAME')],
        [sg.Text('Content:')], [sg.Multiline(key='POST_CONTENT', size=(50, 10))],
        [sg.Button('OK', key='OK'), sg.Button('Cancel', key='CANCEL')]
    ]
    return add_post_layout
