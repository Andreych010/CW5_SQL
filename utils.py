from data_base import *
from config import config
from classes_HH import *


def data_loading(hh_database):
    '''
    Определяет запроссы для классов Employers и Vacancy
    '''
    params = config()
    db = DBCreate(hh_database, params)
    db.create_database()
    list_emp = ['Программный Продукт', 'Softline', 'WebSoft', 'СоюзБалтКомплект', 'Marillion', 'Diasoft', 'JTI', 'IBS', 'INLINE', 'CSBI']
    for i in list_emp:
        hh = Employers(i)
        data = hh.get_request
        for number in range(len(data)):
            id_emp = data[number]["id"]
            vac = Vacancy(id_emp)
            vacancy_list = vac.put_vacancies_in_list()
            db.save_employers_to_database(data)
            db.save_vacancies_to_database(vacancy_list)
