import pandas as pd
from companies import get_companies_df, companies_get_df_by_inn
from participants import get_participants_df
from purchases import get_purschases_df, purschases_get_df_by_inn
from contract import get_contracts_df
from pprint import pprint
from tools import get_full_df, get_df_by_okved, get_json
import json
from tools import to_normal_tuple

pd.options.display.max_rows = 1000
pd.set_option('display.max_columns', 30)


# participants_df = get_participants_df()
# # print("participants_df")
# # print(participants_df.head(5))
# purchases_df = get_purschases_df()
# # print("purchases_df")
# # print(purchases_df.head(5))
# companies_df = get_companies_df()
# # print("companies_df")
# # print(companies_df.head(5))
# contract_df = get_contracts_df()
# # print('contract_df')
# # print(contract_df.head(5))

# print(get_full_df().head(10))


# okpd_df = get_okpd_df()
# okpd_dict = get_okpd_dict()
# print(get_full_df().head(10))

# type:[min, max, mean]


def get_dots_for_regration(okpd: str, time_start: str, time_end: str, delivery_region, type: []) -> ([], [], type):
    df = get_full_df()
    time_start, time_end = min(time_end, time_start), max(time_end, time_start)
    # print(df.head(10))
    sorted_dy_okpd = df[df["lot_name_okpd"] == okpd]
    # sort_by_okved = df[df["okved"] == okved]
    sort_by_region = sorted_dy_okpd[sorted_dy_okpd["delivery_region"] == delivery_region]
    result_df = sort_by_region[sort_by_region["publish_date"] <= time_end]
    result_df = result_df[result_df["publish_date"] >= time_start]
    res = result_df[["publish_date", "price"]]
    return [i for i in result_df["publish_date"]], [i for i in result_df["price"]], type


# print(get_full_df())
from okpd import get_okpd_dict, get_okpd_df, to_normal_tuple

okpd_dict = get_okpd_dict()
print(okpd_dict)
purchases_df = get_purschases_df().head(1000)
# print(purchases_df["lot_name"].map(
#     lambda s: okpd_dict[ss] if ((ss := to_normal_tuple(s)) in okpd_dict.keys()) else None).notnull())
num_good_keys = (purchases_df['lot_name'].map(lambda s: to_normal_tuple(s) in okpd_dict)).sum()
print(purchases_df)
