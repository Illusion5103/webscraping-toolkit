import pandas as pd
df = pd.read_csv('scrape.csv')
df2 = pd.read_csv('scrape2.csv')
df3 = pd.read_csv('scrape3.csv')
df4 = pd.read_csv('scrape4.csv')
df5 = pd.read_csv('scrape5.csv')
frames = [df, df2, df3, df4, df5]
result = pd.concat(frames, ignore_index = True)
result.to_csv('HiddenScrape.csv')