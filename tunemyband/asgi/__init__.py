# tunemyband/asgi/__init__.py
from fastapi.staticfiles import StaticFiles

from .django import application
from .fastapi import app

__all__ = ["app"]

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("", application)
