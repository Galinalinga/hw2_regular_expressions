from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def order_columns(rows):
    result = [' '.join(second_entry[0:3]).split(' ')[0:3] + second_entry[3:7] for second_entry in rows]
    return result

def identify_duplicates(corrected_list):
    witthout_duplicates = []
    for first_entry in corrected_list:
        for second_entry in corrected_list:
            if first_entry[0:2] == second_entry[0:2]:
                list_second_entry = first_entry
                first_entry = list_second_entry[0:2]
                for i in range(2, 7):
                    if list_second_entry[i] == '':
                        first_entry.append(second_entry[i])
                    else:
                        first_entry.append(list_second_entry[i])
        if first_entry not in witthout_duplicates:
            witthout_duplicates.append(first_entry)

    return witthout_duplicates
corrected_list = order_columns(contacts_list) 

print(identify_duplicates(corrected_list))
def unification(rows, regular, new):
    phonebook = []
    pattern = re.compile(regular)
    phonebook = [[pattern.sub(new, string) for string in strings] for strings in rows]

    return phonebook
#
corrected_list = order_columns(contacts_list)
witthout_duplicates_list = identify_duplicates(corrected_list)
regular = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
correct_list = unification(witthout_duplicates_list, regular, r'+7(\2)\3-\4-\5')
regular_2 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
updated_phonebook = unification(correct_list, regular_2, r'+7(\2)\3-\4-\5 доб.\6')

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(updated_phonebook)