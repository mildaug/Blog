from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, sessionmaker
from sqlalchemy import Table, Column

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///blog.db', echo=True)

session = sessionmaker(bind=engine)()

Base.metadata.create_all(engine)


class Users(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    user_name = mapped_column("user_name", String(50))
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

