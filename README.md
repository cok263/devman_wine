# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- [Подготовьте файл с продукцией](#Файл-с-продукцией)
- Запустите сайт с указанием необходимых аргументов
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Пример команды запуска
```
python3 main.py --datafile products.xlsx
```
Возможные аргументы:

--datafile - имя файла с продукцией(по-умолчанию wine.xlsx)

--sheet - название листа с данными(по-умолчанию Лист1)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

## Файл с продукцией

Файл с продукцией должен быть создан в excel. Файл имеет 6 столбцов("Категория", "Название", "Сорт", "Цена", "Картинка", "Акция").
Заполнение столбцов "Категория", "Называние", "Цена", "Картинка" носит обязательный характер. 
Заполнение столбцов "Сорт" и "Акция" опционально.


| Категория      | Название           | Сорт             | Цена | Картинка               | Акция       |
| -------------- | ------------------ | ---------------- | ---- | ---------------------- | ----------- |
| Столовые вина  | Лыхны              | Изабелла         | 350  | likhni.png             |             |
| Десертные вина | Айс Вайн           | Каберне савиньон | 2000 | ice\_wine.png          |             |
| Столовые вина  | Vinal AD Кадарка   | Кадарка          | 300  | vinal\_ad\_kadarka.png | Лучшая цена |
| Десертные вина | Мускат таврический | Мускат           | 395  | muskat\_tavricesky.png |             |