from utils import *


def main():
    params = config()
    db = DBCreate('hh_database', params)
    db.create_database()
    print("Здравствуйте!  ")
    print("Загружаем данные компаний:\n'Программный Продукт', 'Softline', 'WebSoft', 'СоюзБалтКомплект', 'Marillion', 'Diasoft', 'JTI', 'IBS', 'INLINE', 'CSBI'")
    print('Возможно понадобится некоторое время, прийдётся немного подождать \U0001F642...')
    data_loading('hh_database')
    while True:
        db_manager = DBManager('hh_database', params)
        emp_and_count = db_manager.get_companies_and_vacancies_count()
        print('\nНажмите 1, чтобы просмотреть сколько вакансий в компании.')
        print('Нажмите 2, чтобы просмотреть список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию.')
        print('Нажмите 3, чтобы узнать среднюю зарплату.')
        print('Нажмите 4, чтобы узнать вакансии, зарплата по которым выше средней из найденных.')
        print('Нажмите 5, чтобы посмотреть все вакансии по ключевому слову.')
        print('Нажмите 6, чтобы закончить работу программы.')
        user_number = input()
        if user_number == '1':
            print(f"Cписок всех компаний и количество вакансий у каждой компании: \n{emp_and_count}")
        elif user_number == '2':
            print(f"Список компании, вакансии, зарплаты и ссылки на вакансию.: {db_manager.get_all_vacancies()}")
        elif user_number == '3':
            print(f"Средняя зарплата среди всех найденных: {db_manager.get_avg_salary()}")
        elif user_number == '4':
            print(f'Это вакансии, зарплата по которым выше средней из найденных: \n{db_manager.get_vacancies_with_higher_salary()}')
        elif user_number == '5':
            word_key = input('Введите ключевое слово:  ')
            print(f'Вакансии найденые по вашему ключевому слову: \n{db_manager.get_vacancies_with_keyword(word_key)}')
        elif user_number == '6':
            exit('До свидания!')
        else:
            print("Такого варианта нет, попробуйте еще раз")
            print('Вернуться в прежнее меню введите - 1\nиначе программа завершит работу \U0001F910')
            choice = input()
            if choice == '1':
                continue
            else:
                print('Программа закрыта')
                break


if __name__ == '__main__':
    main()