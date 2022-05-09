from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon Name', validators = [DataRequired()])
    submit = SubmitField('I Choose You!')