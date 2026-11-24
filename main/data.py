
import pandas as pd

df =pd.read_csv(r"path_google_csv")

print(df.info())
print(df.head(1))
print(df.tail(1))
print(df.describe())
print(df[df["Type"] == "Paid"]["Price"].min())
print(df[df["Type"] == "Paid"]["Price"].describe())
print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())
print(df[df["Type"] == "Free"])
print(df[df["Type"] == "Paid"])