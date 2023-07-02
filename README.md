### Программа для получения данных о компаниях и вакансиях с сайта [hh.ru](https://hh.ru/?ysclid=ljlgi8kxzx104832045&customDomain=1), проектирует таблицы в БД PostgreSQL и загружает полученные данные в созданные таблицы.

---
Запуск программы происходит из файла `main.py`

Взаимодействие с пользователем осуществляется через следующее меню:
- Введите 1, чтобы просмотреть сколько вакансий в компании.
- Введите 2, чтобы просмотреть список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию.
- Введите 3, чтобы узнать среднюю зарплату.
- Введите 4, чтобы узнать вакансии, зарплата по которым выше средней из найденных.
- Введите 5, чтобы посмотреть все вакансии по ключевому слову.

Создан конфигурационный файл `database.ini` с параметрами подключения к локальной БД postgresql

Пример содержания файла:
```ini
[postgresql]
host=localhost
user=postgres
password=12345
port=5432
```