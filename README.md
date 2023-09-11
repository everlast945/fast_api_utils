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
https://github.com/zhanymkanov/fastapi-best-practices
```

# Команды
```
# Создать миграцию
alembic revision --autogenerate -m "create account table"

```
