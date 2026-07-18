import pandas as pd

FILES = {
    2018: "WALMART DP05/ACSDP5Y2018.DP05-Data.csv",
    2019: "WALMART DP05/ACSDP5Y2019.DP05-Data.csv",
    2020: "WALMART DP05/ACSDP5Y2020.DP05-Data.csv",
    2021: "WALMART DP05/ACSDP5Y2021.DP05-Data.csv",
    2022: "WALMART DP05/ACSDP5Y2022.DP05-Data.csv",
    2023: "WALMART DP05/ACSDP5Y2023.DP05-Data.csv",
    2024: "WALMART DP05/ACSDP5Y2024.DP05-Data.csv"
}

all_years = []

for year, file in FILES.items():

    print(f"Processing {year}...")

    df = pd.read_csv(file)

    # Description row
    desc = df.iloc[0]

    # Actual data
    data = df.iloc[1:].copy()

    def find_col(keyword):
        matches = [
            col for col in df.columns
            if keyword.lower() in str(desc[col]).lower()
        ]
        return matches[0] if matches else None

    cols = {
        "geo_id": "GEO_ID",
        "tract_name": "NAME",
        "population": find_col("Total population"),
        "median_age": find_col("Median age"),
        "under_18_pct": find_col("Under 18 years"),
        "age_65_plus_pct": find_col("65 years and over"),
        "white_pct": find_col("White alone"),
        "black_pct": find_col("Black or African American alone"),
        "asian_pct": find_col("Asian alone"),
        "hispanic_pct": find_col("Hispanic or Latino")
    }

    cols = {k: v for k, v in cols.items() if v is not None}

    temp = data[list(cols.values())].copy()

    temp.columns = list(cols.keys())

    temp["year"] = year

    all_years.append(temp)

final_df = pd.concat(all_years, ignore_index=True)

final_df.to_csv("demographics_clean.csv", index=False)

print(final_df.shape)
print(final_df["year"].value_counts())
print("Saved demographics_clean.csv")
print("\n=== DUPLICATE CHECK ===")
print(
    final_df.duplicated(
        subset=["geo_id", "year"]
    ).sum()
)

print("\n=== MISSING VALUES ===")
print(final_df.isnull().sum())

print("\n=== DATA TYPES ===")
numeric_cols = [
    "population",
    "median_age",
    "under_18_pct",
    "age_65_plus_pct",
    "white_pct",
    "black_pct",
    "asian_pct",
    "hispanic_pct"
]

for col in numeric_cols:
    final_df[col] = pd.to_numeric(final_df[col], errors="coerce")
print(final_df.dtypes)
