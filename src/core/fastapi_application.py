from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


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
        from app.clickhouse_test.router import router as clickhouse_router
        from app.dictionaries.router import router as dictionaries_router

        self.app.include_router(dictionaries_router)
        self.app.include_router(clickhouse_router)
