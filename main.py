from config import session, sg
from blog_backend import Posts, Topics, Users
from frontend.layouts import main_layout
from frontend.views import refresh_post_table, like_post, view_post, add_new_post, edit_post

window = sg.Window("Topics and Posts", main_layout)
table_posts = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    topic = values['TOPIC_COMBO']
    user = values['USER_COMBO']
    if len(table_posts) > 0 and len(values['POST_TABLE']) > 0:
        post = table_posts[values['POST_TABLE'][0]][0]
    else:
        post = None

    if event == 'TOPIC_COMBO':
        table_posts = refresh_post_table(window, topic, user)

    elif event in ['POST_TABLE', 'USER_COMBO']:
        enable_post_adding = isinstance(user, Users) and isinstance(topic, Topics)
        window['ADD_POST_BUTTON'].update(disabled=not enable_post_adding)
        if isinstance(post, Posts):
            window['VIEW_POST_BUTTON'].update(disabled=False)
            if isinstance(user, Users):
                window['LIKE_BUTTON'].update(disabled=False)
            enable_post_editing = enable_post_adding and isinstance(post, Posts) and post.user == user
            window['EDIT_POST_BUTTON'].update(disabled=not enable_post_editing)
    
    elif event == 'VIEW_POST_BUTTON':
        if isinstance(post, Posts):
            view_post(post, user, window)

    elif event == 'LIKE_BUTTON':
        if isinstance(post, Posts) and isinstance(user, Users):
            like_post(post, user, window)

    elif event == 'ADD_TOPIC_BUTTON':
        new_topic_name = sg.popup_get_text('Enter new topic:')
        if len(new_topic_name) > 0 and \
                not session.query(Topics).filter(Topics.name == new_topic_name).first():
            new_topic = Topics(name=new_topic_name)
            session.add(new_topic)
            session.commit()
            window['TOPIC_COMBO'].update(values=session.query(Topics).all())

    elif event == 'ADD_POST_BUTTON':
        if isinstance(topic, Topics) and isinstance(user, Users):
            table_posts = add_new_post(user, topic, window)

    elif event == 'EDIT_POST_BUTTON':
        if isinstance(post, Posts) and isinstance(user, Users) and post.user == user:
            table_posts = edit_post(post, window)

window.close()
