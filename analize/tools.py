import pandas as pd

from companies import get_companies_df, companies_get_df_by_inn
from participants import get_participants_df
from purchases import get_purschases_df, purschases_get_df_by_inn
from contract import get_contracts_df
from okpd import get_okpd_dict, get_okpd_df, to_normal_tuple


def get_full_df() -> pd.DataFrame:
    okpd_dict = get_okpd_dict()
    participants_df = get_participants_df()
    purchases_df = get_purschases_df()
    companies_df = get_companies_df()
    purchases_df["lot_name_okpd"] = purchases_df["lot_name"].map(
        lambda s: okpd_dict[s] if to_normal_tuple(s) in okpd_dict.keys() else None).notnull()

    total_df = purchases_df.merge(participants_df, on="id").merge(companies_df, on="supplier_inn")
    total_df["okved"] = total_df["okved"].map(lambda s: str(s).split(".")[0])
    total_df["publish_date"] = total_df["publish_date"].map(lambda s: str(s).split(" ")[0])
    return total_df


def get_df_by_okved(value: str) -> pd.DataFrame:
    total_df = get_full_df()
    return total_df[total_df["okved"] == str(value)]


def get_json(df: pd.DataFrame):
    return df.to_json






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
