import pandas as pd

movies_df_input = pd.read_csv('movies.csv')
print(movies_df_input.head())
movies_df = pd.DataFrame(movies_df_input['genres'].str.split("|").tolist(), index=movies_df_input.title).stack()
movies_df = movies_df.reset_index([0, 'title'])
movies_df.columns = ['title', 'genre']
movie_cross_table = pd.crosstab(movies_df['title'], movies_df['genre'])
print(movie_cross_table.head())


from scipy.spatial.distance import pdist, squareform

jaccard_dist = pdist(movie_cross_table.values, metric='jaccard')
jaccard_sim_array = 1 - squareform(jaccard_dist)
jaccard_sim_df = pd.DataFrame(jaccard_sim_array, index=movie_cross_table.index, columns=movie_cross_table.index)

# Use it to create a list of movies that we can recommend if you watched The Godfather
jaccard_sim_recom = jaccard_sim_df.loc['Godfather, The (1972)']
recommendations = jaccard_sim_recom.sort_values(ascending=False)
print(recommendations.head(5))

