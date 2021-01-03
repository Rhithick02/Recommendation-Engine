from flask import Flask, render_template, url_for
import pandas as pd

data = pd.read_csv('final2.csv')
movies = list(data['movie_title'].str.capitalize())
director = data['director_name']


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', movies = movies, director = director)

@app.route('/about')
def about():
    return render_template('about.html')