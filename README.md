# API для вопросов и ответов

## Описание
Это REST API для создания и управления вопросами и ответами. 
Проект реализован с помощью Django и Django REST Framework.
Позволяет пользователям создавать вопросы, отвечать на них и просматривать содержимое.

## Стек технологий
- Django 4.x
- Django REST Framework

### Как развернуть проект:

##### Клонировать репозиторий 
```
git clone <https://github.com/GoodWinee/Test-task->
```
##### Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
##### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
python -m pip install --upgrade pip
```
##### Выполнить миграции:
```
python manage.py migrate
```
##### Запустить проект:
```
python manage.py runserver
```
