"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами 'name', 'age' и 'job' и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv

    worker=[
    {'name':'Сергей', 'age':'53', 'job':'токарь'},
    {'name':'Ира', 'age':'35', 'job':'бухгалтер'},
    {'name':'Артемий', 'age':'27', 'job':'инженер'},
    {'name':'Надежда', 'age':'48', 'job':'медсестра'},
    {'name':'Иван', 'age':'30', 'job':'охранник'}
    ]

    with open('company_v1.csv','w', encoding='utf-8', ) as f:
        fields = ['name', 'age', 'job']
        writer= csv.DictWriter(f,fields,delimiter=';')
        writer.writeheader()
        for user in worker:
            writer.writerow(user)


if __name__ == "__main__":
    main()
