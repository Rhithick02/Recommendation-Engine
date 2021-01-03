from flask import Flask, render_template, url_for
import pandas as pd

data = pd.read_csv('final2.csv')
movies = data['movie_title']
director = data['director_name']


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', movies = movies, director = director)

@app.route('/about')
def about():
    return render_template('about.html')