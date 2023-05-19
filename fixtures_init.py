from datetime import date
from blog_backend import Base, Users, Posts, Comments, Topics
from config import session, engine

Base.metadata.create_all(engine)

# Add users
users = []
users.append(Users(username='Kielele', email='kiele@gmail.com', first_name='Leta', last_name='Kiele'))
users.append(Users(username='Mojo', email='linge@gmail.com', first_name='Marius', last_name='Linge'))
users.append(Users(username='Nemunas', email='karietaite@gmail.com', first_name='Gile', last_name='Karietaite'))
users.append(Users(username='Lololo', email='alka@gmail.com', first_name='Lina', last_name='Alka'))
users.append(Users(username='Klaja', email='bukutis@gmail.com', first_name='Martynas', last_name='Bukutis'))
session.add_all(users)

# Add topics
topics = []
topics.append(Topics(id=1, name='Sodininkyste'))
topics.append(Topics(id=2, name='Gamtos mokslai'))
topics.append(Topics(id=3, name='Maisto gaminimas'))
topics.append(Topics(id=4, name='Technologijos'))
topics.append(Topics(id=5, name='Sportas'))
session.add_all(topics)

# Add posts
posts = []
posts.append(Posts(user_id=4, date=date(2023, 5, 11), topic_id=5, name='Eurolyos Final Four Kaune', content='For the first time, Lithuania’s second-biggest city Kaunas will host the Euroleague Final Four. Many basketball fans are looking forward to that event even though their club BC Žalgiris did not make it to the tournament.'))
posts.append(Posts(user_id=1, date=date(2023, 5, 12), topic_id=1, name='Sodininkyste pradedantiems', content='Jeigu neseniai įsigijote namą arba butą su sodu arba sodinių, pirmą sezoną verčiau neskubėti. Po juoda žemes galite atrasti buvusio šeimininko sodo svajones. Daugelis augalų yra daugiamečiai ir žydi kiekvienais metais.'))
posts.append(Posts(user_id=3, date=date(2023, 5, 15), topic_id=4, name='Kas yra ChatGPT?', content='ChatGPT yra pokalbių roboto programa, kuri atsakinėja į tekstinius pranešimus. Tai yra OpenAI sukurtas didelis kalbos modelis, kuris yra mokomas analizuoti ir generuoti tekstą įvairiuose kontekstuose.'))
posts.append(Posts(user_id=5, date=date(2023, 5, 1), topic_id=4, name='Pyweek turnyras', content='Du kartus per metus Python žaidimų kūrėjai renkasi Pyweek turnyre kurti ir varžytis su savo žaidimais.'))
session.add_all(posts)

# Add comments
comments = []
comments.append(Comments(user_id=2, post_id=2, comment="Puikus straipsnis!"))
comments.append(Comments(user_id=1, post_id=1, comment="Nieko gero, nieko naujo nepasakei!"))
comments.append(Comments(user_id=4, post_id=2, comment="Labai gerai pastebeta!"))
session.add_all(comments)

session.commit()
