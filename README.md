# fast_api_utils


## dev install
```bash
# Создание окружения / Установка зависимостей
pyenv install 3.11
pyenv global 3.11
pip install poetry
poetry env use python3.11

```


# Основная структура проекта
```
в корне служебные файлы и зависимости (CI/окружение/документация и т.д.)
backend_fastapi - бэкенд приложение (чтобы отделить от служебных зависимостей) 
- apps - бизнес логика приложения
    - {название модуля}
        - domain (доменные модели)
        - entity (модели сущностей)
        - services (бизнес логика модуля)
- core - ядро (авторизация/настройки/работа консьюмера и т.д.)
- router - интерфейсы взаимодействия с приложением
- utils - различные инструменты (которые поидее могут выноситься в отдельные библиотеки)
- fast_api_application.py (файл запуска самого приложения, рядом будут и другие сервисы kafka-consumer и т.д.)

```