import pandas as pd

mydataset = {
        "cars": ["BMW","Volvo","Ford","Vaxhall","Mercedes","Toyota","Porcshe","Jaguar"],
        "passings": [5, 7, 10, 12, 9, 36, 24, 45]
    }
anyvar = pd.DataFrame(mydataset)
print(anyvar)
