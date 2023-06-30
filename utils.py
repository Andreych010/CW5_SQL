from data_base import *
from config import config
from classes_HH import *


def data_loading(hh_database):
    '''
    Определяет запроссы для классов Employers и Vacancy
    '''
    params = config()  # Модуль подключения к локальному postgresql через файл database.ini
    db = DBCreate(hh_database, params)  # Экземпляр класса DBCreate
    db.create_database()  # Создание БД hh_database
    # Список компаний работодателей
    list_emp = ['Программный Продукт', 'Softline', 'WebSoft', 'СоюзБалтКомплект', 'Marillion', 'Diasoft', 'JTI', 'IBS',
                'INLINE', 'CSBI']

    for i in list_emp:
        hh = Employers(i)  # Экземпляр класса Employers
        data = hh.get_request  # Формируем список работодателей с сайта HeadHunter по нименованию компании работодателя
        for number in range(len(data)):
            id_emp = data[number]["id"]  # Получаем id компании работодателя
            vac = Vacancy(id_emp)  # Экземпляр класса Vacancy
            vacancy_list = vac.put_vacancies_in_list()  # Формируем список словарей найденных компаний
            db.save_employers_to_database(data)  # Заполняем таблицу employers БД hh_database
            db.save_vacancies_to_database(vacancy_list)  # Заполняем таблицу vacancy БД hh_database
