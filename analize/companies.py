import pandas as pd

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 10)


def get_companies_df():
    return pd.read_csv('../data/companies.csv', sep=";")


def companies_get_df_by_inn(inn: int, df: pd.DataFrame) -> pd.DataFrame:
    return df[df["supplier_inn"] == inn]

