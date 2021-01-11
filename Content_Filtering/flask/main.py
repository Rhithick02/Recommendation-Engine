from flask import Flask, render_template, url_for, request
import pandas as pd
from tmdbv3api import Movie, TMDb
import json
import requests

# Converting movies and recommendation to dictionary
df = pd.read_csv('recommend.csv')
data = dict()
for index, row in df.iterrows():
    li = []
    li.append(row[0])
    temp = row[1].lstrip('[').rstrip(']').split(',')
    final = []
    for val in temp:
        val = val.lstrip()
        val = val.rstrip("'").lstrip("'")
        val = val.rstrip('"').lstrip('"')
        final.append(val)
    data[li[0]] = final

# Converting movie and its posterpath to dictionary
df = pd.read_csv('poster_path.csv')
posters = dict()
for index, rows in df.iterrows():
    posters[rows[0]] = rows[1]

# Converting movie and its id to dictionary
df = pd.read_csv('movie_id.csv')
df['movie_id'].fillna(0)
movie_ids = dict()
for index, rows in df.iterrows():
    movie_ids[rows[0]] = rows[1]


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', data = data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/movies')
def hello():
    movie = request.args.get('movieName')
    movie = movie.lower()
    if movie not in data.keys():
        return "<h1> Movie not found in database </h1>"
    else:
        # print(movie)
        return render_template('recommend.html', data = data, name = movie, 
                                posters = posters, m_ids = movie_ids)
