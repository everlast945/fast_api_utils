import asyncio

from core.database_clear import recreate_models


def db_init_models():
    asyncio.run(recreate_models())
    print("Done")


if __name__ == "__main__":
    db_init_models()