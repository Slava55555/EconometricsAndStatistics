import pandas as pd
from collections import Counter

data = pd.read_csv("../data/manga.csv")

data2 = data[["title", "type","status" , "genres", "themes",
              "score", "scored_by", "volumes", "chapters",
              "start_date", "end_date"]]
              
# data2[['end_date']].fillna("2024-04-02 18:07:42+00:00")
# data2['start_date'].fillna("2024-04-02 18:07:42+00:00")
data3 = data2.dropna(subset=["title", "type" , "genres", "themes",
              "score", "scored_by", "volumes", "chapters"])
data4 = data3.fillna("2023-04-02")
print(data['status'].unique())
print(data4.count())

all_themes = [theme for sublist in data["themes"] for theme in sublist]
all_genres = [genre for sublist in data["genres"] for genre in sublist]

genre_counts = Counter(all_genres)
theme_counts = Counter(all_themes)

genre_df = pd.DataFrame(genre_counts.items(), columns=["Genre", "Count"])
genre_df = genre_df.sort_values(by="Count", ascending=False)

theme_df = pd.DataFrame(theme_counts.items(), columns=["Theme", "Count"])
theme_df = theme_df.sort_values(by="Count", ascending=False)

view= 5
top_themes = theme_df.head(view)
top_genres = genre_df.head(view)

for genre in  top_genres:
  data4[f'has {genre}'] = data4['genres'].apply(lambda x: 1 if genre in x else 0)
for theme in  top_themes:
  data4[f'has {theme}'] = data4['themes'].apply(lambda x: 1 if theme in x else 0)



sampled_data = data4.groupby('type', group_keys=False).apply(lambda x: x.sample(min(30, len(x))))
print(sampled_data['type'].value_counts())

print(sampled_data['status'].unique())
sampled_data.to_csv("../data/final.csv")


