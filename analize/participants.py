import pandas as pd
pd.options.display.max_rows = 1000

pd.set_option('display.max_columns', 10)

def get_participants_df():
    return pd.read_csv('../data/participants.csv', sep=";")


# print(df.head(10))
# sorted_df = df.sort_values(by='is_winner', ascending=False)
# print(sorted_df["is_winner"].value_counts())
# print(df.count())
#
# print(df["supplier_inn"])
# print(df.count())

