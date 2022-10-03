from fastapi import FastAPI
from routes.base import api_router as route_v1
from models.message import Message_404, Message_500, Message_Delete, Message_422
#https://www.youtube.com/watch?v=IKmv0AuBwp0


def include_router(app):
    app.include_router(
        route_v1,
        responses={
            404: {"model": Message_404, "description": "Not found"},
            500: {"model": Message_500, "description": "The data sent is not valid"},
            422: {"model": Message_422, "description": "Unprocessable Entity"}
        }
    )

def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()