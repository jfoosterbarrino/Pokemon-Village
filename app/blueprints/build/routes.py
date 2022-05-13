from .import bp as build
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Pokemon, User
from .forms import CatchForm
from app.blueprints.main.forms import PokemonForm
import requests

# @build.route('/catch')
# @login_required
# def catch():
#     form = CatchForm()
#     if request.method == 'POST':
#             pokemon = form.pokemon.data.lower().strip()
#             poke = Pokemon()
#             if len(current_user.pokemen.all()) <= 4:

#                     url =  f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
#                     response = requests.get(url)
#                     if not response.ok:
#                         error_string = 'We had an error'
#                         return render_template('lookup.html.j2', error=error_string)

#                     data = response.json()
#                     poke.name = data["name"]
#                     poke.hp = data["stats"][0]["base_stat"]
#                     poke.ability = data["abilities"][0]["ability"]["name"]
#                     poke.base_exp = data["base_experience"]
#                     poke.sprite = data["sprites"]["other"]["dream_world"]["front_default"]
#                     poke.attack = data["stats"][1]["base_stat"]
#                     poke.defense = data["stats"][2]["base_stat"]
#                     poke.sprite2 = data["sprites"]["front_shiny"]

#                     current_user.collect_poke(poke)
#                     pokemons = current_user.pokemen
            
#                     return render_template('lookup.html.j2', form = form, pokemons =pokemons)

#             flash('You reached MAX of 5 pokemon','danger')
#             return render_template('lookup.html.j2', form = form)
#     return render_template('lookup.html.j2', form = form)

@build.route('/catch/<string:name>')
@login_required
def catch(name):
        if current_user.is_caught(name):
                flash(f'You already have {name}', 'danger')
                return render_template('lookup.html.j2', form =PokemonForm())
        
        if len(current_user.pokemen.all()) <= 4:
                poke = Pokemon.query.filter_by(name = name).first()
                if not poke:
                        poke = Pokemon()

                        url =  f'https://pokeapi.co/api/v2/pokemon/{name}'
                        response = requests.get(url)
                        if not response.ok:
                                error_string = 'We had an error'
                                return render_template('lookup.html.j2', error=error_string)

                        data = response.json()
                        poke.name = data["name"]
                        poke.hp = data["stats"][0]["base_stat"]
                        poke.ability = data["abilities"][0]["ability"]["name"]
                        poke.base_exp = data["base_experience"]
                        poke.sprite = data["sprites"]["other"]["dream_world"]["front_default"]
                        poke.attack = data["stats"][1]["base_stat"]
                        poke.defense = data["stats"][2]["base_stat"]
                        poke.sprite2 = data["sprites"]["front_shiny"]

                current_user.collect_poke(poke)
                flash(f'You have successfully caught {poke.name.title()}','success')
                return render_template('lookup.html.j2', form = PokemonForm())

        flash('You reached MAX of 5 pokemon','danger')
        return render_template('lookup.html.j2', form =PokemonForm())

        

@build.route('/release/<int:id>')
@login_required
def release(id):
        poke = Pokemon.query.get(id)
        current_user.remove_poke(poke)
        flash(f'You have released {poke.name.title()}','warning')
        return redirect(url_for('build.my_pokemon'))

@build.route('/battle')
@login_required
def battle():
        pokemasters = User.query.filter(User.id != current_user.id).all()
        return render_template('battle.html.j2', pokemasters = pokemasters)

    

@build.route('/my_pokemon')
@login_required
def my_pokemon():
        return render_template('my_pokemon.html.j2', pokemons = current_user.pokemen)

@build.route('/attack/<int:id>')
@login_required
def attack(id):
        pokemaster = User.query.get(id)
        cards1 = current_user.pokemen
        cards2 = pokemaster.pokemen
        return render_template('attack.html.j2', cards1 = cards1, cards2 = cards2, pokemaster=pokemaster)

@build.route('/fight/<int:id>')
@login_required
def fight(id):
        pokemaster = User.query.get(id)
        cards1 = current_user.pokemen
        cards2 = pokemaster.pokemen
        if current_user.fight(pokemaster):
                current_user.add_win()
                pokemaster.add_loss()
                flash(f'TEAM {current_user.first_name.upper()} WON!!!','info')
                return render_template('winner.html.j2', cards1 = cards1, cards2 = cards2, user=current_user, i_won =True)
        pokemaster.add_win()
        current_user.add_loss()
        flash(f'TEAM {pokemaster.first_name.upper()} WON!!!','warning')
        return render_template('winner.html.j2', cards1 = cards1, cards2 = cards2, user=current_user, i_won = False)
        
@build.route('/user_info')
@login_required
def user_info():
        return render_template('user_info.html.j2', user = current_user)

        
        