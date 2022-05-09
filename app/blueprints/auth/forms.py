from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo
import random
from jinja2.utils import markupsafe

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Passwords Must Match")])
    submit = SubmitField('Register')


    r1 = random.randint(1,1000)
    r2 = random.randint(1001,2000)
    r3 = random.randint(2001,3000)
    r4 = random.randint(3001,4000)
    r5 = random.randint(4001,5000)
    r6 = random.randint(5001,6000)
    r7 = random.randint(6001,7000)
    r8 = random.randint(7001,8000)
    r9 = random.randint(8001,9000)
    r10 = random.randint(9001,10000)

    # https://avatars.dicebear.com/api/micah/:seed.svg

    r1_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r1}.svg" height = "75px">')
    r2_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r2}.svg" height = "75px">')
    r3_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r3}.svg" height = "75px">')
    r4_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r4}.svg" height = "75px">')
    r5_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r5}.svg" height = "75px">')
    r6_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r6}.svg" height = "75px">')
    r7_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r7}.svg" height = "75px">')
    r8_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r8}.svg" height = "75px">')
    r9_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r9}.svg" height = "75px">')
    r10_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r10}.svg" height = "75px">')

    icon = RadioField('Pick Your Trainer', validators = [DataRequired()],
        choices =[(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img),(r5,r5_img),(r6,r6_img),(r7,r7_img),(r8,r8_img),(r9,r9_img),(r10,r10_img)]
    )


class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Passwords Must Match")])
    submit = SubmitField('Update')


    r1 = random.randint(1,1000)
    r2 = random.randint(1001,2000)
    r3 = random.randint(2001,3000)
    r4 = random.randint(3001,4000)
    r5 = random.randint(4001,5000)
    r6 = random.randint(5001,6000)
    r7 = random.randint(6001,7000)
    r8 = random.randint(7001,8000)
    r9 = random.randint(8001,9000)
    r10 = random.randint(9001,10000)

    # https://avatars.dicebear.com/api/micah/:seed.svg

    r1_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r1}.svg" height = "75px">')
    r2_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r2}.svg" height = "75px">')
    r3_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r3}.svg" height = "75px">')
    r4_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r4}.svg" height = "75px">')
    r5_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r5}.svg" height = "75px">')
    r6_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r6}.svg" height = "75px">')
    r7_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r7}.svg" height = "75px">')
    r8_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r8}.svg" height = "75px">')
    r9_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r9}.svg" height = "75px">')
    r10_img = markupsafe.Markup(f'<img src = "https://avatars.dicebear.com/api/adventurer/{r10}.svg" height = "75px">')

    icon = RadioField('Pick Your Trainer', validators = [DataRequired()],
        choices =[(11000, 'Keep The Same Trainer'),(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img),(r5,r5_img),(r6,r6_img),(r7,r7_img),(r8,r8_img),(r9,r9_img),(r10,r10_img)]
    )