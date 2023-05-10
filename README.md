# fast_api_utils


## dev install
```bash
# Создание окружения / Установка зависимостей
pyenv install 3.11
pyenv global 3.11
pip install poetry
poetry env use python3.11
mkdir .env # (переопределяем настройки из backend_fastapi/core/settings)
alembic upgrade head
cd backend_fastapi
uvicorn fastapi_application:app --reload
```


# Основная структура проекта
```
в корне служебные файлы и зависимости (CI/окружение/документация и т.д.)
alembic - миграции
backend_fastapi - бэкенд приложение (чтобы отделить от служебных зависимостей) 
- apps - бизнес логика приложения
    - entity (модели сущностей)
    - {название модуля}
        - domain (доменные модели)
        - entity (модели сущностей)
        - services (бизнес логика модуля)
- core - ядро (авторизация/настройки/работа консьюмера и т.д.)
- router - интерфейсы взаимодействия с приложением
- utils - различные инструменты (которые поидее могут выноситься в отдельные библиотеки)
- fast_api_application.py (файл запуска самого приложения, рядом будут и другие сервисы kafka-consumer и т.д.)
```

```
# Создать миграцию
alembic revision --autogenerate -m "create account table"

```
