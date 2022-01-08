import pandas as pd

a = [12, 45, 56, 89, 13, 24, 8, 16, 10, 9]
anyvar = pd.Series(a, index= ["Grant","Grace", "Lucy", "Alex","Shane", "Tim", "Dom", "Naka", "Nora","Amos"])
print(anyvar)
print(anyvar["Shane"])



