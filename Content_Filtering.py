import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("main_data.csv")
# print(data)
# features = ['keywords', 'cast', 'genres', 'director']
# for feature in features:
#     data[feature] = data[feature].fillna('')

# def combine_features(row):
#     combine = ""
#     for i in features:
#         combine += str(row[i])
#         combine += " "
#     return combine

# data["combined_features"] = data.apply(combine_features, axis = 1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(data["comb"])
similarity = cosine_similarity(count_matrix)

# def get_title_from_index(index):
# 	return data[data.index == index]["movie_title"].values[0]

# def get_index_from_title(title):
# 	return data[data.movie_title == title]["index"].values[0]

m = 'zathura: a space adventure'
m = m.lower()

similar_movies = []
movie_index = data.loc[data['movie_title']==m].index[0]
similar_movies = similar_movies + list(enumerate(similarity[movie_index]))
sorted_sim_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)

cnt = 0
for movie in sorted_sim_movies:
    print(data['movie_title'][movie[0]])
    cnt = cnt + 1
    if cnt > 20: 
        break
