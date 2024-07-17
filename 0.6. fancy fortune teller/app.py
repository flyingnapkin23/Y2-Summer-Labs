from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("home.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:     
        name = request.form['fname']
        bday = request.form['bday']
        return redirect(url_for('fortune', name = name, birth_date = bday))



@app.route('/fortune/<name>/<birth_date>')
def fortune(name, birth_date):
    fortunes = [
    "Dear {name}, your journey through life will be illuminated by the stars aligned on {birth_date}.",
    "On {birth_date}, {name}, a door to opportunity will swing wide open. Step through boldly!",
    "The universe has special plans for {name}, born on {birth_date}. Expect wonders beyond imagination!",
    "{name}, your creativity will flourish under the celestial energies of {birth_date}. Embrace inspiration!",
    "Born on {birth_date}, {name}, your strength and resilience will overcome any challenge life presents.",
    "Destiny smiles upon {name}, born under the stars of {birth_date}. Adventure awaits around every corner!",
    "On {birth_date}, the cosmos gifted {name} with a heart full of compassion and a spirit of determination.",
    "{name}, your journey began on {birth_date}, marked by the promise of prosperity and joy.",
    "The stars have aligned for {name}, born on {birth_date}, promising a life filled with love and laughter.",
    "On {birth_date}, {name}, the universe bestowed upon you the gift of boundless potential and endless possibilities."
]
    return render_template("fortune.html",fortune = the_fortunes[randint(0,10)])


if __name__ == '__main__':
    app.run(debug = True)