import pandas as pd

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 10)
from companies import get_companies_df, companies_get_df_by_inn
from participants import get_participants_df
from purchases import get_purschases_df, purschases_get_df_by_inn
from contract import get_contracts_df

participants_df = get_participants_df()
# print("participants_df")
# print(participants_df)
purchases_df = get_purschases_df()
# print("purchases_df")
# print(purchases_df)
companies_df = get_companies_df()
# print("companies_df")
# print(companies_df)
contract_df = get_contracts_df()
# print('contract_df')
# print(contract_df)


merged_df = companies_df.merge(participants_df, on='supplier_inn')
print(merged_df.count())
