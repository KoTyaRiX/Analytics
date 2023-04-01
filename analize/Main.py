import pandas as pd
from companies import get_companies_df, companies_get_df_by_inn
from participants import get_participants_df
from purchases import get_purschases_df, purschases_get_df_by_inn
from contract import get_contracts_df
from okpd import get_okpd_dict, get_okpd_df
from pprint import pprint

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 10)

participants_df = get_participants_df()
# print("participants_df")
# print(participants_df.head(5))
purchases_df = get_purschases_df()
# print("purchases_df")
# print(purchases_df.head(5))
companies_df = get_companies_df()
# print("companies_df")
# print(companies_df.head(5))
contract_df = get_contracts_df()
# print('contract_df')
# print(contract_df.head(5))

okpd_df = get_okpd_df()
okpd_dict = get_okpd_dict()

# pprint(okpd_dict)
print(purchases_df.count())
purchases_df["purchase_code"] = purchases_df["purchase_name"]\
    .map(lambda s: okpd_dict[s] if s in okpd_dict.keys() else None)
purchases_df_in_okpd = purchases_df[purchases_df["purchase_code"].notnull()]
print(purchases_df_in_okpd.count())


# print(purchases_df["purchase_name"].)

# merge companies and participants by inn
# merged_df_by_inn = companies_df.merge(participants_df, on='supplier_inn')
# # print(merged_df_by_inn)
#
# # merge by id (purch_...)
# merged_df_by_id = contract_df.merge(participants_df, on='id')
# merged_df_by_id = merged_df_by_id.merge(purchases_df, on="id")
# print(merged_df_by_id)
# print(merged_df_by_id["delivery_region"].value_counts())
# print(contract_df["id"].unique())
