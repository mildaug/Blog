# Komandinė užduotis (BLOG'as):
# Reikalavimai:
# - SQLAlchemy
# - Duomenų modelio sąsajos: išnaudotas many-to-one ryšys, many-to-many būtų pliusas
# - PySimpleGUI pagrindu įgyvendinta vartotojo sąsaja
# - Išskirtas backend (modelis ir bazės sukūrimas) ir frontend (vartotojo sąsaja)
# Objektiškai realizuota vartotojo sąsaja yra didelis pliusas 

from datetime import datetime
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column('user_name', String(50))
    email = Column('email', String(50))
    f_name = Column('f_name', String(50))
    l_name = Column('l_name', String(50))
    # Relationships:
    posts_by_user = relationship("Posts", back_populates="user_post")
    liked_by_user = relationship("Likes", back_populates="user_like")
    commented_by_user = relationship("Comments", back_populates="user_comments")

    def __repr__(self):
        return f"({self.id}, {self.user_name})"


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_name = Column('post_name', String(50))
    content = Column('content', String(300))
    # date = Column('date', String(50))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    # Relationships:
    user_post = relationship("Users", back_populates="posts_by_user")
    posts_in_topic = relationship("Topics", back_populates="topic_with_posts")
    all_likes = relationship("Likes", back_populates="post_like")
    all_comments = relationship("Comments", back_populates="post_comments")

    def __repr__(self):
        return f"({self.id}, {self.user_id}, {self.topic_id})"


class Topics(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    topic_name = Column('topic_name', String(50))
    # Relationships:
    topic_with_posts = relationship("Posts", back_populates="posts_in_topic")

    def __repr__(self):
        return f"({self.id}, {self.topic_name})"


class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    # Relationships:
    user_like = relationship("Users", back_populates="liked_by_user")
    post_like = relationship("Posts", back_populates="all_likes")

    def __repr__(self):
        return f"({self.user_id}, {self.post_id})"
    

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column('comment', String(250))
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    # Relationships:
    user_comments = relationship("Users", back_populates="commented_by_user")
    post_comments = relationship("Posts", back_populates="all_comments")

    def __repr__(self):
        return f"({self.comment}, {self.user_id}, {self.post_id})"


engine = create_engine('sqlite:///blog.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_user(user_name, email, f_name, l_name, ):
    user = Users(user_name=user_name, email=email, f_name=f_name, l_name=l_name)
    session.add(user)
    session.commit()

# add_user('Kielele', 'kiele@gmail.com','Leta', 'Kiele')
# add_user('Mojo', 'linge@gmail.com', 'Marius', 'Linge')
# add_user('Nemunas', 'karietaite@gmail.com', 'Gile', 'Karietaite')
# add_user('Lololo', 'alka@gmail.com', 'Lina', 'Alka')
# add_user('Klaja', 'bukutis@gmail.com', 'Martynas', 'Bukutis')


def get_users():
    users = session.query(Users).all()
    return users

def get_user_by_id(user_id):
    user = session.get(Users, user_id)
    return user

def view_posts():
    posts = session.query(Posts).all()
    for post in posts:
        print(post)
    return posts

def add_posts(user_id, post_name, content, topic_id):
    posts = Posts(user_id=user_id, post_name=post_name, content=content, topic_id=topic_id) # date=datetime.now().strftime("%Y-%m-%d")
    session.add(posts)
    session.commit()

# add_posts(3, "Info apie PhP", "Random tekstas patikrinimui ir peržiūrai ar viskas veikia", 1)

def add_topic(topic_name):
    topic = Topics(topic_name=topic_name)
    session.add(topic)
    session.commit() 

def add_comment(user_id, post_id, comment):
    comment = Comments(user_id=user_id, post_id=post_id, comment=comment)
    session.add(comment)
    session.commit()

# add_comment(2,2, "Puikus straipsnis!")
# add_comment(1,1, "Nieko gero, nieko naujo nepasakei!")

# add_topic("Informatika")

def view_topic():
    all_topics = session.query(Topics).all()
    for topic in all_topics:
        print(topic)
    return all_topics

def post_topic_join_by_topicid(topic_id):
    query = session.query(Posts, Topics).select_from(Posts).join(Topics).filter(Topics.id == topic_id)
    joined_table = query.all()

    for post, topic in joined_table:
        print(f"Post Name: {post.post_name}, Topic Name: {topic.topic_name}")
    
    return joined_table

def info_table_join_by_postid(post_id):
    query = session.query(Posts, Topics, Users).select_from(Posts).join(Topics).join(Users).filter(Posts.id == post_id)
    joined_table = query.all()

    for post, topic, user in joined_table:
        print(f"Username: {user.user_name}, Post name: {post.post_name}, Post content: {post.content} Topic: {topic.topic_name}")

    return joined_table

def get_comments_by_postid(post_id):
    comments = session.query(Comments, Users).join(Users).filter(Comments.post_id == post_id).all()
    return comments

def print_post_comments(post_id):
    comments = get_comments_by_postid(post_id)
    for comment, user in comments:
        print(f"---------------------------")
        print(f"---------Komentaras--------")
        print(f"Comment: {comment.comment}")
        print(f"User: {user.user_name}")

# print_post_comments(2)
# print_post_comments(1)

# post_topic_join_by_topicid(1)
# info_table_join_by_postid(2)
# info_table_join_by_postid(3)
