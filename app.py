from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route ('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/lookup', methods =['GET','POST'])
def lookup():

    if request.method == 'POST':
        pokemon = request.form.get('pokemon')

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
        
        return render_template('lookup.html.j2', pokemons=new_data)


    return render_template('lookup.html.j2')
