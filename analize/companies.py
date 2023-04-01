import pandas as pd

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 10)


def get_df_by_inn(inn: int) -> pd.DataFrame:
    df = pd.read_csv('../data/companies.csv', sep=";")
    return df[df["supplier_inn"] == inn]
