import pickle
import pandas as pd
from preprocessing import convert, convert_cast, fetch_director, remove_space, stems
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

movies = movies.merge(credits,on='title')

# Keeping important columns for recommendation
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
movies.dropna(inplace=True)


movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)  # handle keywords
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x:x.split())  # handle overview (converting to list)

movies['cast'] = movies['cast'].apply(remove_space)
movies['crew'] = movies['crew'].apply(remove_space)
movies['genres'] = movies['genres'].apply(remove_space)
movies['keywords'] = movies['keywords'].apply(remove_space)

# Concatenate all
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# dropping those extra columns
new_df = movies[['movie_id', 'title', 'tags']]

# Converting list to str
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Converting to lower case
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())
new_df['tags'] = new_df['tags'].apply(stems)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vector)


pickle.dump(new_df,open('artifacts/movie_list.pkl','wb'))
pickle.dump(similarity,open('artifacts/similarity.pkl','wb'))

