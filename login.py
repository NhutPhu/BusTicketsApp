import flet as ft
from app.utils.constant import HEIGHT, WIDTH

def login(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Sign in"
    page.bgcolor = ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors = [
            "#E0F2FE",  
            "#60A5FA",  
            "#1E3A8A"
        ],  
    )
    
    try:
        page.window.width = WIDTH
        page.window.height = HEIGHT
        page.window.resizable = False
    except Exception:
        pass
    page.update()

    user_label = ft.Text("User Name", size=14, width=100, text_align=ft.TextAlign.LEFT)
    userName = ft.TextField(
        hint_text="Enter username", 
        width=200,
        border_color=ft.Colors.WHITE
    )

    pass_label = ft.Text("Password", size=14, width=100, text_align=ft.TextAlign.LEFT)
    password = ft.TextField(
        hint_text="Enter password", 
        width=200, 
        password=True,
        border_color=ft.Colors.WHITE
    )
    

    checkBox = ft.Checkbox(
        label="Agree the terms",
        value=False,
        active_color=ft.Colors.BLUE_600,
        shape=ft.RoundedRectangleBorder(radius=4),
        label_style=ft.TextStyle(weight=ft.FontWeight.W_300),
        border_side=ft.BorderSide(
            color=ft.Colors.BLUE_600,
            width=2,
            stroke_align=ft.BorderSideStrokeAlign.INSIDE
        )
    )

    submitButton = ft.ElevatedButton(
        "Sign in",
        width=100,
        disabled=True,
        bgcolor=ft.Colors.BLUE_ACCENT,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(alignment=ft.alignment.center)
    )

    def validate(e):
        if all([userName.value and userName.value.strip(), password.value and password.value.strip(), checkBox.value]):
            submitButton.disabled = False
        else:
            submitButton.disabled = True
        page.update()

    def submit(e):
        print(f"User Name: {userName.value}")
        print(f"Password: {password.value}")

        page.clean()
        page.add(
            ft.Row(
                controls=[
                    ft.Text(
                        f"Welcome {userName.value} to Bus Tickets App",
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                        size=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkBox.on_change = validate
    userName.on_change = validate
    password.on_change = validate
    submitButton.on_click = submit

    user_row = ft.Row(
        controls=[user_label, userName],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    pass_row = ft.Row(
        controls=[pass_label, password],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    form_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(
                            src="assets/images/bus.png",
                            fit=ft.ImageFit.CONTAIN,
                            height=40,
                            width=40
                        )
                        ,
                        ft.Text("Bus Tickets App", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                user_row,
                pass_row,
                ft.Row(controls=[checkBox], alignment=ft.MainAxisAlignment.START),
                ft.Row(controls=[submitButton], alignment=ft.MainAxisAlignment.CENTER)
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.all(16),
        width=350,
        height=400,
        bgcolor=ft.Colors.WHITE,
        border_radius=8,
        shadow=ft.BoxShadow(blur_radius=12, color=ft.Colors.BLACK12)
    )

    page.clean()
    page.clean()

    gradient_bg = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "#E0F2FE",
                "#60A5FA",
                "#1E3A8A"
            ]
        ),
        content=ft.Row(
            controls=[form_container],  # form login của bạn
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.add(gradient_bg)

    page.update()
