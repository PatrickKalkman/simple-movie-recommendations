import pandas as pd

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Create a new column in the ratings_df called an map it to the title of the movie
ratings_df['title'] = ratings_df['movieId'].map(movies_df.set_index('movieId')['title'])
print(ratings_df.head())

# Build recommendation 1, most seen movies.
print(ratings_df['title'].value_counts().head(10))


# Build recommendation 2, highest rates movies.
avg_rating_df = ratings_df[['title', 'rating']].groupby(['title']).mean()
sorted_avg_rating_df = avg_rating_df.sort_values(by='rating', ascending=False)
print(sorted_avg_rating_df.head())

print((ratings_df['title'] == 'Alien Escape (1995)').sum())
print((ratings_df['title'] == 'Boiling Point (1993)').sum())
print((ratings_df['title'] == 'Borgman (2013)').sum())
print((ratings_df['title'] == 'Bone Tomahawk (2015)').sum())
print((ratings_df['title'] == 'Borgman (2013)').sum())


movie_seen_frequency = ratings_df['title'].value_counts()
reviewed_books = movie_seen_frequency[movie_seen_frequency > 100].index
frequent_movies_df = ratings_df[ratings_df['title'].isin(reviewed_books)]
frequent_movies_avg_rating_df = frequent_movies_df[['title', 'rating']].groupby(['title']).mean()
print(frequent_movies_avg_rating_df.sort_values(by='rating', ascending=False).head())


# Build recommendation 3
print("Building recommendation 3")
from itertools import permutations

def find_movie_pairs(item):
    movie_pairs = pd.DataFrame(list(permutations(item.values, 2)), columns=['movie_a', 'movie_b'])
    return movie_pairs


movie_combinations = ratings_df.groupby('userId')['title'].apply(find_movie_pairs).reset_index(drop=True)
print(movie_combinations)

combination_counts = movie_combinations.groupby(['movie_a', 'movie_b']).size()
combination_counts_df = combination_counts.to_frame(name='size').reset_index()
combination_counts_df.sort_values('size', ascending=False, inplace=True)
print(combination_counts_df.head(5))

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

# Find the movies most frequently watched by people who watched The Godfather
godfather_df = combination_counts_df[combination_counts_df['movie_a'] == 'Godfather, The (1972)'].head(5)
print(godfather_df)

# Plot the results
godfather_df.plot.bar(x="movie_b")
plt.show()