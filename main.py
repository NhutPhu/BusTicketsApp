from app.pages.login import login
from app.routes import getRoute
import flet as ft

def main(page: ft.Page):
    getRoute(page, "/login")

if __name__ == "__main__":
    ft.app(target=main)