from datetime import date
from config import session, sg
from blog_backend import Topics, Users, Posts, Likes
from frontend.layouts import view_post_layout, add_post_layout

def refresh_post_table(window: sg.Window, topic: Topics, user: Users):
    posts = session.query(Posts).filter(Posts.topic == topic).all()
    table_posts = [[post, post.date, len(post.likes)] for post in posts]
    window['POST_TABLE'].update(table_posts)
    window['VIEW_POST_BUTTON'].update(disabled=True)
    window['LIKE_BUTTON'].update(disabled=True)
    enable_post_adding = isinstance(user, Users) and isinstance(topic, Topics)
    window['ADD_POST_BUTTON'].update(disabled=not enable_post_adding)
    window['EDIT_POST_BUTTON'].update(disabled=True)
    return table_posts

def view_post(post: Posts, user: Users, window: sg.Window):
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

def like_post(post: Posts, user: Users, window: sg.Window):
    current_like = session.query(Likes).filter(Likes.user == user, Likes.post == post).first()
    if not current_like:
        new_like = Likes(user=user, post=post)
        session.add(new_like)
    else:
        session.delete(current_like)
    session.commit()
    refresh_post_table(window, post.topic, user)

def add_new_post(user: Users, topic: Topics, window: sg.Window):
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
    return refresh_post_table(window, topic, user)

def edit_post(post: Posts, window: sg.Window):
    edit_post_window = sg.Window(f"Editing Post: {post.name}", add_post_layout(), finalize=True)
    edit_post_window['POST_NAME'].update(post.name)
    edit_post_window['POST_CONTENT'].update(post.content)
    while True:
        event, values = edit_post_window.read()
        if event in (sg.WINDOW_CLOSED, 'Close', 'CANCEL'):
            break
        if event == 'OK':
            if len(values['POST_NAME']) > 0 and len(values['POST_CONTENT']) > 0:
                post.name = values['POST_NAME']
                post.content = values['POST_CONTENT']
                post.date=date.today()
                session.commit()
                break
            else:
                sg.popup_error('You have left something empty. Both title and content must contain something.', title='Empty Fields')
    edit_post_window.close()
    return refresh_post_table(window, post.topic, post.user)
