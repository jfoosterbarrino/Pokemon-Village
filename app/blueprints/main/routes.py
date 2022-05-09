from flask import render_template, request
import requests
from .forms import PokemonForm
from . import bp as main
from flask_login import login_required


@main.route ('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2')


@main.route('/lookup', methods =['GET','POST'])
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