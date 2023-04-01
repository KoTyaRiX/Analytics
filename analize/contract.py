import pandas as pd

pd.options.display.max_rows = 1000


def get_contracts_df():
    df = pd.read_csv('../data/contracts.csv', sep=";")
    return df[df["contract_reg_number"].notnull()]
