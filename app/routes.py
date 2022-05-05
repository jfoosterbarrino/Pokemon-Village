from flask import render_template, request, flash, redirect, url_for
import requests
from .forms import LoginForm, RegisterForm, PokemonForm
from app import app
from .models import User
from flask_login import current_user, login_user, logout_user, login_required

@app.route ('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data

        user = User.query.filter_by(email = email).first()
        if user and user.check_hashed_password(password):
            login_user(user)
            flash('Successful Login! Welcome to PokeVillage!', 'success')
            return redirect(url_for('index'))
        flash('Incorrect Email and/or Password. Try again.', 'danger')
        return render_template('login.html.j2', form =form)
    return render_template('login.html.j2', form = form)

@app.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have been logged out', 'info')
        return redirect(url_for('login'))


@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data={
            'first_name' : form.first_name.data.title(),
            'last_name' : form.last_name.data.title(),
            'email' : form.email.data.lower(),
            'password' : form.password.data
        }

        new_user_object = User()
        new_user_object.from_dict(new_user_data)
        new_user_object.save()

        flash('Congratulations! You have successfully registered.','success')
        return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('register.html.j2', form = form)

    else:
        flash('Unsuccessful Login, Please Try Again Later','danger')
        return render_template('register.html.j2', form =form)


@app.route('/lookup', methods =['GET','POST'])
@login_required
def lookup():
    form = PokemonForm()

    if request.method == 'POST':
        pokemon = form.pokemon.data.lower()

        url =  f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if not response.ok:
            error_string = 'We had an error'
            return render_template('lookup.html.j2', error=error_string)

        data = response.json()
        new_data = []
        pokemon_data = {
            "name": data["name"],
            "ability": data["abilities"][0]["ability"]["name"],
            "base_experience": data["base_experience"],
            "sprite": data["sprites"]["front_shiny"],
            "base_attack": data["stats"][1]["base_stat"],
            "base_hp": data["stats"][0]["base_stat"],
            "base_defense": data["stats"][2]["base_stat"]
        }
        new_data.append(pokemon_data)
        
        return render_template('lookup.html.j2', pokemons=new_data, form = form)


    return render_template('lookup.html.j2', form=form)