import flet as ft
from app.pages.login import login

def getRoute(page=ft.Page, path=str):
    if path == "/login":
        login(page)