import pandas as pd
pd.options.display.max_rows = 1000

pd.set_option('display.max_columns', 10)

df = pd.read_csv('../data/participants.csv', sep=";")

# withoot_null_df = df[df["contract_reg_number"].notnull()]

print(df.head(10))
sorted_df = df.sort_values(by='is_winner', ascending=False)
print(sorted_df["is_winner"].value_counts())
print(df.count())

