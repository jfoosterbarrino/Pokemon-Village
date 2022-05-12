from flask import render_template, request, flash
import requests
from .forms import PokemonForm
from . import bp as main
from flask_login import login_required, current_user


@main.route ('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2', user = current_user)


@main.route('/lookup', methods =['GET','POST'])
@login_required
def lookup():
    form = PokemonForm()

    if request.method == 'POST':
        pokemon = form.pokemon.data.lower()

        url =  f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if not response.ok:
            flash('Pokemon does not exist','danger')
            return render_template('lookup.html.j2',  form = form)

        data = response.json()
        new_data = []
        pokemon_data = {
            "name": data["name"],
            "ability": data["abilities"][0]["ability"]["name"],
            "base_exp": data["base_experience"],
            "sprite": data["sprites"]["other"]["dream_world"]["front_default"],
            "attack": data["stats"][1]["base_stat"],
            "hp": data["stats"][0]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "sprite2": data["sprites"]["front_shiny"]
        }
        new_data.append(pokemon_data)
        
        return render_template('lookup.html.j2', pokemons=new_data, form = form)


    return render_template('lookup.html.j2', form=form)