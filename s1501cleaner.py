import pandas as pd

FILES = {
    2018: "WALMART S1501/ACSST5Y2018.S1501-Data.csv",
    2019: "WALMART S1501/ACSST5Y2019.S1501-Data.csv",
    2020: "WALMART S1501/ACSST5Y2020.S1501-Data.csv",
    2021: "WALMART S1501/ACSST5Y2021.S1501-Data.csv",
    2022: "WALMART S1501/ACSST5Y2022.S1501-Data.csv",
    2023: "WALMART S1501/ACSST5Y2023.S1501-Data.csv",
    2024: "WALMART S1501/ACSST5Y2024.S1501-Data.csv"
}

KEEP_COLS = {
    "GEO_ID": "geo_id",
    "NAME": "tract_name",
    "S1501_C01_014E": "hs_grad_or_higher",
    "S1501_C01_015E": "bachelors_or_higher",
    "S1501_C01_012E": "bachelors_degree",
    "S1501_C01_013E": "graduate_degree"
}

all_years = []

for year, file in FILES.items():

    print(f"\nProcessing {year}...")

    df = pd.read_csv(file, low_memory=False)

    # Remove description row
    df = df.iloc[1:].copy()

    temp = df[list(KEEP_COLS.keys())].copy()

    temp.rename(columns=KEEP_COLS, inplace=True)

    temp["year"] = year

    all_years.append(temp)

final_df = pd.concat(all_years, ignore_index=True)

numeric_cols = [
    "hs_grad_or_higher",
    "bachelors_or_higher",
    "bachelors_degree",
    "graduate_degree"
]

for col in numeric_cols:
    final_df[col] = pd.to_numeric(
        final_df[col],
        errors="coerce"
    )

final_df.to_csv(
    "education_clean.csv",
    index=False
)

print("\n====================")
print("SHAPE")
print("====================")
print(final_df.shape)

print("\n====================")
print("ROWS PER YEAR")
print("====================")
print(final_df["year"].value_counts().sort_index())

print("\n====================")
print("DUPLICATES")
print("====================")
print(
    final_df.duplicated(
        subset=["geo_id", "year"]
    ).sum()
)

print("\n====================")
print("MISSING VALUES")
print("====================")
print(final_df.isnull().sum())

print("\n====================")
print("SUMMARY")
print("====================")
print(
    final_df[numeric_cols].describe()
)

print("\nSaved: education_clean.csv")