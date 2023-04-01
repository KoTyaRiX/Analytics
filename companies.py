import pandas as pd
pd.options.display.max_rows = 1000

pd.set_option('display.max_columns', 10)

df = pd.read_csv('.\data\companies.csv', sep=";")

# withoot_null_df = df[df["contract_reg_number"].notnull()]

print(df.count())
print(df[df["status"] != "Активная"].count())
