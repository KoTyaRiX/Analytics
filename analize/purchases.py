import pandas as pd

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 10)


def get_purschases_df():
    return pd.read_csv('../data/purchases.csv', sep=";")


def purschases_get_df_by_inn(inn: int, df: pd.DataFrame) -> pd.DataFrame:
    return df[df["supplier_inn"] == inn]


_df = get_purschases_df()

# withoot_null_df = df[df["contract_reg_number"].notnull()]

# print(_df.head(10))
# print(_df.sort_values(by="contract_category", ascending=False)["contract_category"].value_counts())
