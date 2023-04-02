import pandas as pd

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def to_normal_tuple(s: str) -> tuple:
    mas = str(s).replace(",", " ").replace(";", " ").split(" ")
    answer = []
    for word in mas:
        answer.append(morph.parse(word)[0].normal_form)
    return tuple(sorted(set(answer)))


def get_okpd_df() -> pd.DataFrame:
    return pd.read_excel(io="../data/okpd.xlsx", engine='openpyxl', usecols="B:C", header=6)


def get_okpd_dict() -> dict:
    df = get_okpd_df()
    df["Код"] = df["Код"].map(lambda s: str(s).split(".")[0])
    df["Название"] = df["Название"].map(lambda s: to_normal_tuple(s))
    okpd_dict = {}
    for (k, v) in zip(df["Название"], df["Код"]):
        okpd_dict[k] = v
    return okpd_dict
