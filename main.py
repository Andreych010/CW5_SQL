from utils import *


def main():
    params = config()  # Модуль подключения к локальному postgresql через файл database.ini
    print('Здравствуйте!')
    print("Загружаем данные компаний:\n'Программный Продукт', 'Softline', 'WebSoft', "
          "'СоюзБалтКомплект', 'Marillion', 'Diasoft', 'JTI', 'IBS', 'INLINE', 'CSBI'")
    print('Возможно понадобится некоторое время, прийдётся немного подождать \U0001F642...')
    data_loading('hh_database')  # Загружает БД hh_database

    # Цикл взаимодействия с пользователем, через класс DBManager БД hh_database
    while True:
        db_manager = DBManager('hh_database', params)  # Экземпляр класса DBManager
        print('\nВведите 1, чтобы просмотреть сколько вакансий в компании.')
        print('Введите 2, чтобы просмотреть список всех вакансий с указанием названия компании,'
              ' вакансии, зарплаты и ссылки на вакансию.')
        print('Введите 3, чтобы узнать среднюю зарплату.')
        print('Введите 4, чтобы узнать вакансии, зарплата по которым выше средней из найденных.')
        print('Введите 5, чтобы посмотреть все вакансии по ключевому слову.')
        print('Введите 6, чтобы закончить работу программы.')
        user_number = input()
        if user_number == '1':
            print(f'Cписок всех компаний и количество вакансий у каждой компании:')
            db_manager.get_companies_and_vacancies_count()
        elif user_number == '2':
            print(f'Список компаний, вакансий, зарплаты и ссылки на вакансию.:')  # \n{db_manager.get_all_vacancies()}')
            db_manager.get_all_vacancies()
            # db_manager.get_all_vacancies()
        elif user_number == '3':
            print(f"Средняя зарплата среди всех найденных: \n{db_manager.get_avg_salary()}")
        elif user_number == '4':
            print(f'Это вакансии, зарплата по которым выше средней из найденных:')  # \n{db_manager.get_vacancies_with_higher_salary()}')
            db_manager.get_vacancies_with_higher_salary()
        elif user_number == '5':
            word_key = input('Введите ключевое слово:  ')
            print(f'Вакансии найденые по вашему ключевому слову:')  # \n{db_manager.get_vacancies_with_keyword(word_key)}')
            db_manager.get_vacancies_with_keyword(word_key)
        elif user_number == '6':
            exit('До свидания!')
        else:
            print('Такого варианта нет, попробуйте еще раз')
            print('Вернуться в прежнее меню введите - 1\nиначе программа завершит работу \U0001F910')
            choice = input()
            if choice == '1':
                continue
            else:
                print('Программа закрыта')
                break


if __name__ == '__main__':
    main()
