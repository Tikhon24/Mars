from flask import Flask
from flask import render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from forms.login_user import LoginForm
from forms.add_work import WorkForm
from data import db_session
from data import users, jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(users.User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/index')
def index():
    title = 'Mars'
    return render_template('base.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/work/add', methods=['GET', 'POST'])
def add_work():
    form = WorkForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        work = jobs.Job()
        work.job = form.job.data
        work.team_leader = team_leader_id = form.team_leader.data
        work.work_size = form.work_size.data
        work.collaborators = collaborators_id = form.collaborators.data
        work.is_finished = form.is_finished.data
        team_leader = db_sess.query(users.User).filter(users.User.id == team_leader_id).first()
        team_leader.jobs.append(work)
        db_sess.merge(team_leader)
        for user in [db_sess.query(users.User).filter(users.User.id == int(id)).first() for id in
                     collaborators_id.split(', ')]:
            user.jobs.append(work)
            db_sess.merge(user)
        db_sess.commit()
        return redirect('/')
    return render_template('add_work.html', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
