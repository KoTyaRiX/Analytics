import pymorphy2
morph = pymorphy2.MorphAnalyzer()
def to_normal_tuple(s: str) -> tuple:
    mas = s.replace(",", " ").replace(";", " ").split(" ")
    answer = []
    for word in mas:
        answer.append(morph.parse(word)[0].normal_form)
    return tuple(sorted(set(answer)))


# words = ['котиков', 'кошечек', 'мышонков']
#
# for word in words:
#     parsed_word = morph.parse(word)[0] # Получаем Parse-объект для слова
#     normal_form = parsed_word.normal_form  # Получаем нормальную форму слова
#     parsed_normal_form = morph.parse(normal_form)[0]  # Получаем Parse-объект для нормальной формы слова
#     stem = parsed_normal_form.stem  # Получаем основу слова
#     print(stem)

print(to_normal_tuple("Оказание услуг по обеспечению физической охраны объекта ГБОУ школа № 655 Приморского района Санкт-Петербурга по адресу Богатырский пр-т, д. 48, корп. 2, лит. А в период с 10.01.2022г. по 31.03.2022г."))