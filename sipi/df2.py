import pandas as pd
data = {
    "calories": [420, 380, 390, 600, 400, 456, 267, 100],
    "duration": [50, 40, 45, 70, 47, 60, 35, 18]
}
myvar = pd.DataFrame(data)
print(myvar)
print(myvar.loc[[1,2]])

myvar = pd.DataFrame(data,index=["day1","day2","day3","day4","day5","day6","day7","day8"])
print(myvar)

