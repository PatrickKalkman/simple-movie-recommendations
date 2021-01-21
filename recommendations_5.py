import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#pd.set_option('display.max_columns', None)

movies_input = pd.read_csv('movies_with_synopsis.csv')
movies_input = movies_input.dropna()

vectorizer = TfidfVectorizer(min_df=3, max_df=0.7)
vectorized_data = vectorizer.fit_transform(movies_input['synopsis'])
tfidf_df = pd.DataFrame(vectorized_data.toarray(), columns=vectorizer.get_feature_names())
tfidf_df.index = movies_input['title']
print(tfidf_df.head())

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity_array = cosine_similarity(tfidf_df)
cosine_similarity_df = pd.DataFrame(cosine_similarity_array, index=tfidf_df.index, columns=tfidf_df.index)
cosine_similarity_series = cosine_similarity_df.loc['Toy Story (1995)']
ordered_similarities = cosine_similarity_series.sort_values(ascending=False)

print(ordered_similarities.head(6))
