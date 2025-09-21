import pandas as pd
import os

df = pd.read_csv(r"C:\Users\Varun\Downloads\Saurav\Class_Records\MlopsNitish-Singh\DataUsed\Ecommerce Customers.csv")

df = df.iloc[:, 3:]

df = df[df["Length of Membership"] > 3]

df.to_csv(os.path.join("data","customers.csv"),index = False)
