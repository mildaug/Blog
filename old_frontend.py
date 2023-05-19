from sqlalchemy.orm import sessionmaker
from config import session, sg

# all_topics = view_topic()
# topics = [topics.topic_name for topics in all_topics]

# all_posts = view_posts()
# posts = [post.post_name for post in all_posts]

# all_users = get_users()
# user = [[user.id, user.user_name] for user in all_users]

# likes = defaultdict(dict) 

# def get_post_content(topic, post_name):
#     topic_object = session.query(Topics).filter(Topics.topic_name == topic).first()
#     post = session.query(Posts).filter(Posts.topic_id == topic_object.id, Posts.post_name == post_name).first()
#     print(post)
#     if post:
#         return post.content
#     else:
#         return ""
    
# def view_post_layout(content=''):
#     layout = [
#         [sg.Text('Post details')],
#         [sg.Multiline(content, size=(50, 10), key='POST_CONTENT', disabled=True)],
#         [sg.Button('Close')]
#     ]
#     return layout   

# def add_post_layout():
#     add_post_layout = [
#         [sg.Text('Enter post details:')],
#         [sg.Text('Username:'), sg.Combo(user, key='user_name')],
#         [sg.Text('Post Name:'), sg.Input(key='post_name')],
#         [sg.Text('Content:'), sg.Input(key='content')],
#         [sg.Text('Topic:'), sg.Combo(topics, key='topic_combo')],
#         [sg.Button('OK', key='OK'), sg.Button('Cancel', key='CANCEL')]
#     ]   
#     return add_post_layout

# def add_like_layout():
#     add_like_layout = [
#         [sg.Text('Who adds a like: '), sg.Combo(user, key='user_name')],
#         [sg.Button('OK', key='OK'), sg.Button('Cancel', key='CANCEL')]
#     ]
#     return add_like_layout

window = sg.Window("Topics and Posts", main_layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'TOPIC_COMBO':
        posts = session.query(Posts).filter(Posts.topic == values['TOPIC_COMBO']).all()
        table_posts = [[post, post.date, len(post.likes)] for post in posts]
        window['POST_TABLE'].update(table_posts)

        # selected_topic = values['TOPIC_COMBO']
        # print(selected_topic, type(selected_topic))
        # post_table = window['POST_TABLE']
        # post_list = posts
        # post_table.update(values=[[post, likes[selected_topic].get(post, 0)] for post in post_list])

    # if event == 'FILTER_BUTTON':
    #     selected_topic = values['TOPIC_COMBO']
    #     post_table = window['POST_TABLE']
    #     all_posts = post_topic_join_by_topicname(selected_topic)
    #     selected_posts = []
    #     for post, topic in all_posts:
    #         likes_count = session.query(Likes).filter_by(post_id=post.id).distinct(Likes.user_id).count()
    #         selected_post = [post.post_name, post.date, likes_count]
    #         selected_posts.append(selected_post)
    #     post_table.update(values=selected_posts)

    # if event == 'ADD_TOPIC_BUTTON':
    #     new_topic = sg.popup_get_text('Enter new topic:')
    #     if new_topic:
    #         add_topic(new_topic)
    #         topics.append(new_topic)
    #         window['TOPIC_COMBO'].update(values=topics)

    # if event == 'ADD_POST_BUTTON':
    #     layout = add_post_layout()
    #     add_post_window = sg.Window('Add Post', layout)
    #     while True:
    #         event, values = add_post_window.read()
    #         if event == sg.WINDOW_CLOSED:
    #             break
    #         elif event == "CANCEL":
    #             add_post_window.close()
    #         elif event == 'OK':
    #             new_post_username = values['user_name']
    #             new_post_id = new_post_username[0]
    #             new_post_name = values['post_name']
    #             new_post_content = values['content']
    #             new_post_date = datetime.now().strftime("%Y-%m-%d")
    #             selected_topic = values['topic_combo']
    #             topic_id = next(topic.id for topic in all_topics if topic.topic_name == selected_topic)
    #             new_post = add_posts(new_post_id, new_post_name, new_post_content, new_post_date, topic_id)
    #             add_post_window.close()

    # if event == 'VIEW_POST_BUTTON':
    #     selected_row = values['POST_TABLE'][0]
    #     selected_post = selected_posts[selected_row]
    #     selected_post_name = selected_post[0]
    #     print(selected_post_name)
    #     post_content = get_post_content(selected_topic, selected_post_name)
    #     layout = view_post_layout(post_content)
    #     view_post_window = sg.Window('View Post', layout, finalize=True)
    #     view_post_window['POST_CONTENT'].update(value=post_content)
    #     while True:
    #         event, values = view_post_window.read()
    #         if event in (sg.WINDOW_CLOSED, 'Close'):
    #             break
    #     view_post_window.close()

    # if event == 'LIKE_BUTTON':
    #     layout = add_like_layout()
    #     add_like_window = sg.Window('Add Post', layout)
    #     selected_row = values['POST_TABLE'][0]
    #     selected_post_name = selected_posts[selected_row][0]
    #     print(selected_post_name)
    #     post_id = get_post_id(selected_post_name)
    #     print(post_id)
    #     while True:
    #         event, values = add_like_window.read()
    #         if event == sg.WINDOW_CLOSED:
    #             break
    #         elif event == "CANCEL":
    #             add_like_window.close()
    #         elif event == "OK":
    #             selected_user = values['user_name']
    #             selected_user_id = selected_user[0]
    #             print(selected_user_id)
    #             if selected_user:
    #                 add_like(selected_user_id, post_id, sg)
    #                 add_like_window.close()
