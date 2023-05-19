from sqlalchemy import Integer, String, ForeignKey, Column, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column('username', String(50))
    email = Column('email', String(50))
    first_name = Column('first_name', String(50))
    last_name = Column('last_name', String(50))
    # Relationships:
    posts = relationship("Posts", back_populates="user")
    likes = relationship("Likes", back_populates="user")
    comments = relationship("Comments", back_populates="user")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"({self.id}, {self.username})"
    
    def __str__(self):
        return self.full_name
    

class Topics(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    # Relationships:
    posts = relationship("Posts", back_populates="topic")

    def __repr__(self):
        return f"({self.id}, {self.name})"

    def __str__(self):
        return self.name


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column('name', String(50))
    content = Column('content', String(300))
    date = Column('date', Date)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    # Relationships:
    topic = relationship("Topics", back_populates="posts")
    user = relationship("Users", back_populates="posts")
    likes = relationship("Likes", back_populates="post")
    comments = relationship("Comments", back_populates="post")
   
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    # Relationships:
    user = relationship("Users", back_populates="likes")
    post = relationship("Posts", back_populates="likes")
    
    def __repr__(self):
        return f"({self.user_id}, {self.post_id})"
    

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column('comment', String(250))
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    # Relationships:
    user = relationship("Users", back_populates="comments")
    post = relationship("Posts", back_populates="comments")

    def __repr__(self):
        return f"({self.comment}, {self.user_id}, {self.post_id})"
