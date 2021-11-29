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
    {'name':'Sergey', 'age':'53', 'job':'turner'},
    {'name':'Ira', 'age':'35', 'job':'accountant'},
    {'name':'Artemiy', 'age':'27', 'job':'engineer'},
    {'name':'Nadin', 'age':'48', 'job':'nurse'},
    {'name':'ivan', 'age':'30', 'job':'security'}
    ]

    with open('company_v2.csv','w', encoding='utf-8', ) as f:
        fields = ['name', 'age', 'job']
        writer= csv.DictWriter(f,fields,delimiter=';')
        writer.writeheader()
        for user in worker:
            writer.writerow(user)


if __name__ == "__main__":
    main()
