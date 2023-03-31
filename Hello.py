import pandas as pd

df = pd.read_csv('.\data\contracts.csv', sep=";")

withoot_null_df = df[df["contract_reg_number"].notnull()]

counts = withoot_null_df['id'].value_counts()
# сортируем результат по индексу
sorted_counts = counts.sort_index()
# объединяем результат с исходным DataFrame по столбцу id
result_df = pd.merge(withoot_null_df, sorted_counts,
                     left_on='id', right_index=True, suffixes=("", "_count"))
# сортируем по количеству уникальных значений в порядке убывания
df = result_df.sort_values(by='id_count', ascending=False)
# df = df.rename(columns={"id_y": "id_count"})
print("by id count")
print(df)

counts = withoot_null_df['contract_reg_number'].value_counts()
# сортируем результат по индексу
sorted_counts = counts.sort_index()
# объединяем результат с исходным DataFrame по столбцу id
result_df = pd.merge(withoot_null_df, sorted_counts, left_on='contract_reg_number', right_index=True, suffixes=("", "_count"))
# сортируем по количеству уникальных значений в порядке убывания
df = result_df.sort_values(by='contract_reg_number_count', ascending=False)

print("by contract_reg_number count")
print(df)

# withoot_null_df["cool_id"] = df["id"].map(lambda s:s[6::])


# print(withoot_null_df.head(10000).tail(5))
# print(withoot_null_df.tail(5))
# print(withoot_null_df.keys())
# print(len(df))
# print(len(withoot_null_df))

group_by_contr_df = withoot_null_df.groupby(['contract_reg_number'])

print(group_by_contr_df.head(5))
group_by_purch_df = withoot_null_df.groupby(['contract_reg_number'])
print(group_by_contr_df.head(5))
