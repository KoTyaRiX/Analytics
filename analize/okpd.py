import pandas as pd


def get_okpd_df() -> pd.DataFrame:
    return pd.read_excel(io="../data/okpd.xlsx", engine='openpyxl', usecols="B:C", header=6)


def get_okpd_dict() -> dict:
    df = get_okpd_df()
    df["Код"] = df["Код"].map(lambda s: str(s).split(".")[0])
    okpd_dict = {}
    for (k, v) in zip(df["Название"], df["Код"]):
        okpd_dict[k] = v
    return okpd_dict
