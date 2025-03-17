from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    team_leader = StringField('Лидер команды (id)', validators=[DataRequired()])
    work_size = IntegerField('Размер работы в часах')
    collaborators = StringField('Сотрудники (id)')
    is_finished = BooleanField('Работа окончена?')
    submit = SubmitField('Добавить')
