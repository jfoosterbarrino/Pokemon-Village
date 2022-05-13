from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default = dt.utcnow)
    icon = db.Column(db.Integer)
    pokemen = db.relationship('Pokemon',
                    cascade = "all, delete",
                    secondary = 'pokemon_user',
                    backref= 'users',
                    lazy='dynamic'
                    )
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)

    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'

    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'

    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
        self.icon = data['icon']
        self.wins = 0
        self.losses = 0


    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_icon_url(self):
        return f'https://avatars.dicebear.com/api/adventurer/{self.icon}.svg'
    

    def collect_poke(self, poke):
        self.pokemen.append(poke)
        db.session.commit()

    def remove_poke(self,poke):
        self.pokemen.remove(poke)
        db.session.commit()

    def is_caught(self, pokemon_name):
        return self.pokemen.filter(Pokemon.name == pokemon_name).count() > 0
    
    def add_win(self):
        self.wins += 1
        db.session.commit()

    def add_loss(self):
        self.losses += 1
        db.session.commit()
    
    def fight(self, opponent):
        counter = 0
        for index in list(range(5)):
            if (self.pokemen[index].hp + self.pokemen[index].attack + self.pokemen[index].defense) > (opponent.pokemen[index].hp + opponent.pokemen[index].attack + opponent.pokemen[index].defense):
                counter += 1
        return counter >= 3

    
            


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Pokemon(db.Model):
    poke_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ability = db.Column(db.String)
    base_exp = db.Column(db.Integer)
    sprite = db.Column(db.String)
    attack = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sprite2 = db.Column(db.String)

class PokemonUser(db.Model):
    poke_id = db.Column(db.Integer, db.ForeignKey('pokemon.poke_id'), primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)