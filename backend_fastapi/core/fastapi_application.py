from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.films import router as films_router
from routers.dictionaries import router as dictionaries_router
from routers.persons import router as persons_router

class SettingApplication:
    def __init__(self) -> None:
        super().__init__()
        self.app = FastAPI()
    def get_application(self):
        self._set_middlewares()
        self._set_routers()
        return self.app
    def _set_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    def _set_routers(self):
        self.app.include_router(dictionaries_router)
        self.app.include_router(persons_router)
        self.app.include_router(films_router)
