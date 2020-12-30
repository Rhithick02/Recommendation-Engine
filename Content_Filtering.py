import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataframe = pd.read_csv("movie_dataset.csv")
features = ['keywords', 'cast', 'genres', 'director']
for feature in features:
    dataframe[feature] = dataframe[feature].fillna('')

def combine_features(row):
    combine = ""
    for i in features:
        combine += str(row[i])
        combine += " "
    return combine

dataframe["combined_features"] = dataframe.apply(combine_features, axis = 1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(dataframe["combined_features"])
similarity = cosine_similarity(count_matrix)

def get_title_from_index(index):
	return dataframe[dataframe.index == index]["title"].values[0]

def get_index_from_title(title):
	return dataframe[dataframe.title == title]["index"].values[0]

movies_user_likes = ['The Avengers']
similar_movies = []
for movie_user_likes in movies_user_likes:
    movie_index = get_index_from_title(movie_user_likes)
    similar_movies = similar_movies + list(enumerate(similarity[movie_index]))
    sorted_sim_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)

cnt = 0
for movie in sorted_sim_movies:
    print(get_title_from_index(movie[0]))
    cnt = cnt + 1
    if cnt > 20: 
        break
