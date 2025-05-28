import pandas as pd

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

out = data4.sample(10000)
print(out['status'].unique())
out.to_csv("../data/final.csv")


