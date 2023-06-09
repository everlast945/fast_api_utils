import glob
from os.path import basename, dirname, isfile, join

# Импортируем все файлы из entity, чтобы сразу alembic видел все модели
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')
]
