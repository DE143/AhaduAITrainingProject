import pathlib
import pandas as pd

base_dir = pathlib.Path(__file__).resolve().parent
csv_path = base_dir / "ecommerce.csv"

df = pd.read_csv(csv_path)
# print(df.head(2))

# print("\n")
# print("\n")
# print("\n")

# print(df.info())
# print("\n")
# age_under_30 = df[df["age"] <= 30]
# print(age_under_30.head(30))

print(df["gender"].head(10))