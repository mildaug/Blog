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
    # Relationships:
    posts_by_user = relationship("Posts", back_populates="user_post")

    def __repr__(self):
        return f"({self.id}, {self.user_name})"


class Posts(Base):
    __tablename__ = "posts"
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column("user_id", Integer, ForeignKey("users.id"))
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

while True:
    choice = input('''[===Choose===]: 
1 - View posts
2 - Add posts
''').strip()

    try:
        choice = int(choice)
    except ValueError:
        pass

    if choice == 1:
        posts = session.query(Posts).all()
        for post in posts:
            print(post)

    if choice == 2:
        user_id = input('Enter user ID: ')
        topic_id = input('Enter topic ID: ')

        posts = Posts(user_id=user_id, topic_id=topic_id)
        session.add(posts)
        session.commit()

# add topic main layout
# view users, add users, second layout - K
# view posts, add posts, second layout - M
# view comments, add comments, second layout
# view likes, add like, second layout