-- Создание, удаление базы данных hh_database
DROP DATABASE IF EXISTS hh_database;
CREATE DATABASE hh_database;

-- Создание таблицы employers
CREATE TABLE employers (
                    id_employer INT PRIMARY KEY,
                    name_employer VARCHAR(255) NOT NULL,
                    open_vacancies VARCHAR,
                    url_employer TEXT
                );

-- Создание таблицы vacancies
CREATE TABLE vacancies (
                    id_vacancy INT PRIMARY KEY,
                    name_vacancy VARCHAR(255) NOT NULL,
                    id_employer INT REFERENCES employers(id_employer),
                    name_employer VARCHAR NOT NULL,
                    salary_from INT,
                    salary_to INT,
                    salary_avg INT,
                    city VARCHAR(255),
                    experience TEXT,
                    requirement TEXT,
                    url TEXT
                );

-- Заполнение таблицы employers
INSERT INTO employers (id_employer, name_employer, open_vacancies, url_employer)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (id_employer) DO NOTHING
                    RETURNING id_employer;

-- Заполнение таблицы vacancies
INSERT INTO vacancies (id_vacancy, name_vacancy, id_employer, name_employer, city, salary_from,
                    salary_to, salary_avg, experience, requirement, url)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

-- Возвращает список всех компаний и количество вакансий у каждой компании.
SELECT name_employer, open_vacancies FROM employers;

-- Возвращает список всех вакансий с указанием названия компании, названия вакансии
-- и зарплаты, и ссылки, на вакансию.
SELECT name_employer, name_vacancy, salary_from, salary_to, url FROM vacancies;

-- Возвращает среднюю зарплату по вакансиям.
SELECT ROUND(AVG(salary_avg)) as avg_salary FROM vacancies WHERE salary_from>0 AND salary_to>0;

-- Возвращает список всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT name_employer, name_vacancy, salary_avg, url FROM vacancies
WHERE salary_avg > (SELECT AVG(salary_avg) FROM vacancies WHERE salary_from>0 AND salary_to>0);

-- Возвращает список всех вакансий, в названии которых содержатся переданные в метод слова.
SELECT * FROM vacancies WHERE name_vacancy ILIKE '%python%';

