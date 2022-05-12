from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CatchForm(FlaskForm):
    pokemon = StringField('Pokemon Name', validators = [DataRequired()])
    submit = SubmitField("CATCH 'EM")