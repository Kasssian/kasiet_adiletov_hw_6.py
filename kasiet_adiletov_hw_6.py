import re

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    name_list = re.findall(r"\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b", content)
    email_list = re.findall(r'[a-z0-9]+@\S{1,}', content)
    file_list = re.findall(r'[A-Za-z]+\.(?!com|net|org|edu|gov|mil|info|int)[a-z3]{3,5}', content)
    colour_list = re.findall(r'#[a-f0-9]{6}', content)
while True:
    user = int(input('Выберите данные,которые хотите переписать(1(Ф.И.),2(почта),3(файлы),4(цвет),5(выход)): '))
    if user == 1:
        with open('name_list.txt', 'w') as name_file:
            name_file.write(str(name_list))
            name_file.close()
    elif user == 2:
        with open('email_list.txt', 'w') as email_file:
            email_file.write(str(email_list))
            email_file.close()
    elif user == 3:
        with open('type_file.txt', 'w') as type_file:
            type_file.write(str(file_list))
            type_file.close()
    elif user == 4:
        with open('colour_file.txt', 'w') as colour_file:
            colour_file.write(str(colour_list))
            colour_file.close()
    elif user == 5:
        break
    else:
        print('Вы не правильно ввели запрос,повторите попытку.')
        continue
