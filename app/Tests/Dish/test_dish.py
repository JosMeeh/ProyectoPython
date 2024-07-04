from fastapi import FastAPI, status
from httpx import AsyncClient


class TestDishRoutes:
    async def test_create_task_route_exists(
        self, app: FastAPI, client: AsyncClient
    ) -> None:
        res = await client.post(app.url_path_for("Dish"), json={})
        assert res.status_code != status.HTTP_404_NOT_FOUND