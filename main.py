from flask import Flask
from data import db_session
from data import users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    db_sess = db_session.create_session()

    user = users.User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.adress = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)

    user = users.User()
    user.surname = 'Winchester'
    user.name = 'Dean'
    user.age = 30
    user.position = 'officer'
    user.speciality = 'hunter'
    user.adress = 'module_2'
    user.email = 'dean_hunt@mars.org'
    db_sess.add(user)

    user = users.User()
    user.surname = 'Winchester'
    user.name = 'Sam'
    user.age = 26
    user.position = 'officer'
    user.speciality = 'hunter'
    user.adress = 'module_2'
    user.email = 'sam_hunt@mars.org'
    db_sess.add(user)

    user = users.User()
    user.surname = 'Smith'
    user.name = 'Castiel'
    user.age = 4000
    user.position = 'officer'
    user.speciality = 'secretary'
    user.adress = 'module_3'
    user.email = 'castiel_angel@mars.org'
    db_sess.add(user)

    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
