import pandas as pd

path = 'https://www.w3schools.com/python/pandas/data.js'
df = pd.read_json(path)
print(df.to_string())