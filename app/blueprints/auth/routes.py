from flask import render_template, request, flash, redirect, url_for
from .forms import LoginForm, RegisterForm, EditProfileForm
from . import bp as auth
from ...models import User
from flask_login import current_user, login_user, logout_user, login_required

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data

        user = User.query.filter_by(email = email).first()
        if user and user.check_hashed_password(password):
            login_user(user)
            flash('Successful Login! Welcome to PokeVillage!', 'success')
            return redirect(url_for('main.index'))
        flash('Incorrect Email and/or Password. Try again.', 'danger')
        return render_template('login.html.j2', form =form)
    return render_template('login.html.j2', form = form)

@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have been logged out', 'info')
        return redirect(url_for('auth.login'))


@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data={
            'first_name' : form.first_name.data.title(),
            'last_name' : form.last_name.data.title(),
            'email' : form.email.data.lower(),
            'password' : form.password.data,
            'icon' : form.icon.data,
            'wins' : 0,
            'losses' : 0
        }

        new_user_object = User()
        new_user_object.from_dict(new_user_data)
        new_user_object.save()

        flash('Congratulations! You have successfully registered.','success')
        return redirect(url_for('auth.login'))

    elif request.method == 'GET':
        return render_template('register.html.j2', form = form)

    else:
        flash('Unsuccessful Login, Please Try Again Later','danger')
        return render_template('register.html.j2', form =form)


@auth.route('/edit_profile', methods = ['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data={
                "first_name": form.first_name.data.title(),
                "last_name": form.last_name.data.title(),
                "email": form.email.data.lower(),
                "password": form.password.data,
                "icon": int(form.icon.data) if int(form.icon.data) != 11000 else current_user.icon
            }
        user = User.query.filter_by(email = new_user_data['email']).first()
        if user and user.email != current_user.email:
            flash('Email is already in use', 'danger')
            return redirect(url_for('auth.edit_profile'))
        try:
            current_user.from_dict(new_user_data)
            current_user.save()
            flash('Profile Updated','success')
        except:
            flash('There was an unexpected error, please try again!','danger')
            return redirect(url_for('auth.edit_profile'))
        return redirect(url_for('main.index'))
    return render_template('register.html.j2', form = form)



