import pandas as pd

FILES = {
    2018: "WALMART S1901/ACSST5Y2018.S1901-Data.csv",
    2019: "WALMART S1901/ACSST5Y2019.S1901-Data.csv",
    2020: "WALMART S1901/ACSST5Y2020.S1901-Data.csv",
    2021: "WALMART S1901/ACSST5Y2021.S1901-Data.csv",
    2022: "WALMART S1901/ACSST5Y2022.S1901-Data.csv",
    2023: "WALMART S1901/ACSST5Y2023.S1901-Data.csv",
    2024: "WALMART S1901/ACSST5Y2024.S1901-Data.csv"
}

KEEP_COLS = {
    "GEO_ID": "geo_id",
    "NAME": "tract_name",
    "S1901_C01_001E": "households_total",
    "S1901_C01_012E": "median_household_income",
    "S1901_C01_013E": "mean_household_income",
    "S1901_C01_007E": "households_50k_74k",
    "S1901_C01_008E": "households_75k_99k",
    "S1901_C01_009E": "households_100k_149k",
    "S1901_C01_010E": "households_150k_199k",
    "S1901_C01_011E": "households_200k_plus"
}

all_years = []

for year, file in FILES.items():

    print(f"Processing {year}")

    df = pd.read_csv(file, low_memory=False)

    # Remove description row
    df = df.iloc[1:].copy()

    temp = df[list(KEEP_COLS.keys())].copy()

    temp.rename(columns=KEEP_COLS, inplace=True)

    temp["year"] = year

    all_years.append(temp)

final_df = pd.concat(all_years, ignore_index=True)

numeric_cols = [
    "households_total",
    "median_household_income",
    "mean_household_income",
    "households_50k_74k",
    "households_75k_99k",
    "households_100k_149k",
    "households_150k_199k",
    "households_200k_plus"
]

for col in numeric_cols:
    final_df[col] = pd.to_numeric(
        final_df[col],
        errors="coerce"
    )

final_df.to_csv(
    "income_clean.csv",
    index=False
)

print("\nSHAPE")
print(final_df.shape)

print("\nROWS PER YEAR")
print(final_df["year"].value_counts().sort_index())

print("\nDUPLICATES")
print(
    final_df.duplicated(
        subset=["geo_id", "year"]
    ).sum()
)

print("\nMISSING VALUES")
print(final_df.isnull().sum())

print("\nSUMMARY")
print(
    final_df[
        numeric_cols
    ].describe()
)

print("\nSaved: income_clean.csv")