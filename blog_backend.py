# Komandinė užduotis (BLOG'as):
# Reikalavimai:
# - SQLAlchemy
# - Duomenų modelio sąsajos: išnaudotas many-to-one ryšys, many-to-many būtų pliusas
# - PySimpleGUI pagrindu įgyvendinta vartotojo sąsaja
# - Išskirtas backend (modelis ir bazės sukūrimas) ir frontend (vartotojo sąsaja)
# Objektiškai realizuota vartotojo sąsaja yra didelis pliusas 

from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, sessionmaker
from sqlalchemy import Table, Column

class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    user_name = mapped_column("user_name", String(50))
    email = mapped_column("email", String(50))
    f_name = mapped_column("first_name", String(50))
    l_name = mapped_column("last_name", String(50))
    # Relationships:
    posts_by_user = relationship("Posts", back_populates="user_post")

    def __repr__(self):
        return f"({self.id}, {self.user_name})"


class Posts(Base):
    __tablename__ = "posts"
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column("user_id", Integer, ForeignKey("users.id"))
    post_name = mapped_column("post_name", String(50))
    content = mapped_column("content", String(300))
    topic_id = mapped_column("topic_id", Integer, ForeignKey("topics.id"))
    # Relationships:
    user_post = relationship("Users", back_populates="posts_by_user")
    posts_in_topic = relationship("Topics", back_populates="topic_with_posts")

    def __repr__(self):
        return f"({self.id}, {self.user_id}, {self.topic_id})"


class Topics(Base):
    __tablename__ = "topics"
    id = mapped_column(Integer, primary_key=True)
    topic_name = mapped_column("topic_name", String(50))
    # Relationships:
    topic_with_posts = relationship("Posts", back_populates="posts_in_topic")

    def __repr__(self):
        return f"({self.id}, {self.topic_name})"


engine = create_engine('sqlite:///blog.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, f_name, l_name, email):
    user = Users(user_name=username, f_name=f_name, l_name=l_name, email=email)
    session.add(user)
    session.commit()

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
    posts = Posts(user_id=user_id, post_name=post_name, content=content, topic_id=topic_id)
    session.add(posts)
    session.commit()

def add_topic(topic_name):
    topic = Topics(topic_name=topic_name)
    session.add(topic)
    session.commit()

def view_topic():
    all_topics = session.query(Topics).all()
    for topic in all_topics:
        print(topic)
    return all_topics

# view comments, add comments, second layout
# view likes, add like, second layout

