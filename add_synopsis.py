import pandas as pd
import requests
import time

pd.set_option('display.max_columns', None)

movies_df_input = pd.read_csv('movies.csv')
movies_links = pd.read_csv('links.csv')

movies_df_input['imdbId'] = movies_links['imdbId']
movies_df_input['synopsis'] = ''

movies_df_input = movies_df_input.set_index('movieId')

print(movies_df_input.head())

for row in movies_df_input.itertuples():
    try:
        imdb = str(row.imdbId).zfill(7)
        request_url = f'http://www.omdbapi.com/?i=tt{imdb}&plot=full'
        response = requests.get(request_url)
        json = response.json()
        print(f'{json["Title"]} {imdb}')
        movies_df_input.at[row.Index, 'synopsis'] = json['Plot']
    except Exception as e:
        print(e)

    time.sleep(.200)

movies_df_input.to_csv('movies_with_synopsis.csv')

print(movies_df_input.head())

