import PySimpleGUI as sg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blog.db')
session = sessionmaker(bind=engine)()

sg.theme('DarkAmber')
sg.set_options(font=('Sans', 16))
