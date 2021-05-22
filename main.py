from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

pattern_number = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
sub_number = r'+7(\4)\8-\11-\14\15\17\18\19\20'
pattern_name = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
sub_name = r'\1\3\10\4\6\9\7\8'
contacts_result_number = []
contacts_result_name = []
contacts_pre_result = []
contacts_pre_result_2 = []
contacts_result = []

for contacts_1 in contacts_list:
    contacts_str_1 = ','.join(contacts_1)
    result_number = re.sub(pattern_number, sub_number, contacts_str_1)
    split_result_number = result_number.split(',')
    contacts_result_number.append(split_result_number)


for contacts_2 in contacts_result_number:
    contacts_str_2 = ','.join(contacts_2)
    result_name = re.sub(pattern_name, sub_name, contacts_str_2)
    split_result_name = result_name.split(',')
    contacts_result_name.append(split_result_name)

for items in contacts_result_name:
    contacts_pre_result.append(items[0])
    contacts_pre_result.append(items[1])
    if items[2] != '':
        contacts_pre_result.append(items[2])
    if items[3] != '':
        contacts_pre_result.append(items[3])
    if items[4] == 'position':
        contacts_pre_result.append(items[4])
    elif items[4] == '':
        contacts_pre_result.append('')
    else:
        contacts_pre_result.append(items[4])
    if items[5] != int:
        for number in contacts_result_name:
            if number[0] == items[0] and number[1] == items[1] and number[5] != '':
                contacts_pre_result.append(number[5])
    if items[6] != str:
        for email in contacts_result_name:
            if email[0] == items[0] and email[1] == items[1] and email[6] != '':
                contacts_pre_result.append(email[6])
    contacts_pre_result_2.append(contacts_pre_result)
    contacts_pre_result = []

count = 0

for duplicate in contacts_pre_result_2:
    for temp in contacts_result:
        if duplicate[0] == temp[0] and duplicate[1] == temp[1]:
            count += 1
    if count == 0:
        contacts_result.append(duplicate)
    count = 0

pprint(contacts_result)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", newline="", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_result)
