# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# import  collections
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
# duplicate_elements = {}
# for item in new_list:
#     if item in duplicate_elements:
#         duplicate_elements[item] += 1
#     else:
#         duplicate_elements[item] = 1
# print(duplicate_elements)
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
#
# count_frequency = collections.Counter(new_list)
# print(dict(count_frequency))
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
#
# count_frequency = filter(lambda  x: new_list.count(x)>1, new_list)
# count_frequency = list(set(new_list))
#
# print(count_frequency)
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
#
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
