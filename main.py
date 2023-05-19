from datetime import date
from blog_backend import Posts, Likes, Topics, Users
from config import session, sg
from frontend.layouts import main_layout, view_post_layout, add_post_layout

window = sg.Window("Topics and Posts", main_layout)

table_posts = []

def refresh_post_table(window: sg.Window):
    topic = values['TOPIC_COMBO']
    user = values['USER_COMBO']
    posts = session.query(Posts).filter(Posts.topic == topic).all()
    table_posts = [[post, post.date, len(post.likes)] for post in posts]
    window['POST_TABLE'].update(table_posts)
    window['VIEW_POST_BUTTON'].update(disabled=True)
    window['LIKE_BUTTON'].update(disabled=True)
    enable_post_adding = isinstance(user, Users) and isinstance(topic, Topics)
    window['ADD_POST_BUTTON'].update(disabled=not enable_post_adding)
    return table_posts

def view_post(post: Posts, user: Users, window: sg.Window = window):
    view_post_window = sg.Window("View Post", view_post_layout(post), finalize=True)
    if not isinstance(user, Users):
        view_post_window['LIKE_BUTTON'].update(disabled=True)
    while True:
        event, values = view_post_window.read()
        if event in (sg.WINDOW_CLOSED, 'Close'):
            break
        if event == 'LIKE_BUTTON':
            like_post(post, user, window)
    view_post_window.close()

def like_post(post: Posts, user: Users, window: sg.Window = window):
    current_like = session.query(Likes).filter(Likes.user == user, Likes.post == post).first()
    if not current_like:
        new_like = Likes(user=user, post=post)
        session.add(new_like)
        session.commit()
        refresh_post_table(window)
    else:
        session.delete(current_like)
        session.commit()
        refresh_post_table(window)

def add_new_post(user: Users, topic: Topics, window: sg.Window = window):
    print(user, topic)
    new_post_window = sg.Window("Add New Post", add_post_layout(), finalize=True)
    while True:
        event, values = new_post_window.read()
        if event in (sg.WINDOW_CLOSED, 'Close', 'CANCEL'):
            break
        if event == 'OK':
            if len(values['POST_NAME']) > 0 and len(values['POST_CONTENT']) > 0:
                new_post = Posts(
                    name=values['POST_NAME'], 
                    content=values['POST_CONTENT'], 
                    user=user, 
                    topic=topic,
                    date=date.today(),
                )
                session.add(new_post)
                session.commit()
                break
            else:
                sg.popup_error('You have left something empty. Both title and content must contain something.', title='Empty Fields')
    new_post_window.close()
    return refresh_post_table(window)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'TOPIC_COMBO':
        table_posts = refresh_post_table(window)

    if event in ['POST_TABLE', 'USER_COMBO']:
        topic = values['TOPIC_COMBO']
        user = values['USER_COMBO']
        if len(table_posts) > 0 and len(values['POST_TABLE']) > 0:
            window['VIEW_POST_BUTTON'].update(disabled=False)
            if isinstance(user, Users):
                window['LIKE_BUTTON'].update(disabled=False)
        enable_post_adding = isinstance(user, Users) and isinstance(topic, Topics)
        window['ADD_POST_BUTTON'].update(disabled=not enable_post_adding)
    
    if event == 'VIEW_POST_BUTTON':
        if table_posts and len(table_posts) > 0:
            post = table_posts[values['POST_TABLE'][0]][0]
            user = values['USER_COMBO']
            view_post(post, user, window)

    if event == 'LIKE_BUTTON':
        if table_posts and len(table_posts) > 0 and isinstance(values['USER_COMBO'], Users):
            post = table_posts[values['POST_TABLE'][0]][0]
            user = values['USER_COMBO']
            like_post(post, user, window)

    if event == 'ADD_TOPIC_BUTTON':
        new_topic_name = sg.popup_get_text('Enter new topic:')
        if len(new_topic_name) > 0 and \
                not session.query(Topics).filter(Topics.name == new_topic_name).first():
            new_topic = Topics(name=new_topic_name)
            session.add(new_topic)
            session.commit()
            window['TOPIC_COMBO'].update(values=session.query(Topics).all())

    if event == 'ADD_POST_BUTTON':
        table_posts = add_new_post(values['USER_COMBO'], values['TOPIC_COMBO'], window)

window.close()
