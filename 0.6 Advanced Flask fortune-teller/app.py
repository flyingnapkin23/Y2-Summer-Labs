from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("home.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/fortune')
def fortune():
    the_fortunes = ["A pleasant surprise is waiting for you around the corner."
,"Your creativity will lead you to success in unexpected ways.","An old friend will reenter your life with exciting news.","Take a leap of faith and you will be pleasantly surprised.","Good things come to those who wait patiently."
,"Trust your instincts; they will guide you wisely."
,"A recent setback will soon lead to a great opportunity."
,"Generosity will bring you unexpected blessings.","Your determination will open new doors for you.","A journey of a thousand miles begins with a single step."] 
    return render_template("fortune.html",fortune = the_fortunes[randint(0,10)])


if __name__ == '__main__':
    app.run(debug = True)