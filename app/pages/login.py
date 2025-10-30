import flet as ft
from app.utils.constant import HEIGHT, WIDTH

def login(page: ft.Page):
    page.title = "Login Page"
    page.window.width = WIDTH
    page.window.height = HEIGHT
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.maximizable = False
    page.window.resizable = False
    page.alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    TEXT_COLOR = ft.Colors.BLACK
    HINT_COLOR = "#5B7083"

    # --- Ảnh logo ---
    bus_image = ft.Container(
        ft.CircleAvatar(
            content=ft.Image(
                src="assets/images/bus_logo.png",
                width=40,
                color="#E0F7FA",
            ),
            bgcolor=ft.Colors.BLUE,
            radius=40,
        ),
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(0, 3),
            blur_style=ft.ShadowBlurStyle.INNER
        ),
        border_radius=50
    )

    # --- Username ---
    user_label = ft.Text(
        "Username", 
        color=TEXT_COLOR, 
        size=14,
        weight=ft.FontWeight.W_600
    )
    user_field = ft.TextField(
        prefix_icon=ft.Icons.PERSON,
        hint_text="Type your username",
        hint_style=ft.TextStyle(color=HINT_COLOR),
        border=ft.InputBorder.UNDERLINE,
        border_color=TEXT_COLOR,
        width=250,
    )
    input_user = ft.Column(
        controls=[user_label, user_field],
        spacing=5,
        width=250,
    )

    # --- Password ---
    password_label = ft.Text(
        "Password", 
        color=TEXT_COLOR, 
        size=14,
        weight=ft.FontWeight.W_600
    )
    password_field = ft.TextField(
        prefix_icon=ft.Icon(
            name=ft.Icons.LOCK,   
        ),
        hint_text="Type your password",
        hint_style=ft.TextStyle(color=HINT_COLOR),
        border=ft.InputBorder.UNDERLINE,
        password=True,
        can_reveal_password=True,
        border_color=TEXT_COLOR,
        width=250,
    )
    forgot_password = ft.TextButton(
        text="Forgot password?",
        style=ft.ButtonStyle(
            color=ft.Colors.LIGHT_BLUE_900,
            padding=6,
            text_style=ft.TextStyle(
                size=12,
                weight=ft.FontWeight.W_600
            )
        ),
    )

    input_password = ft.Column(
        controls=[
            password_label,
            password_field,
            ft.Row(
                controls=[forgot_password],
                alignment=ft.MainAxisAlignment.END,
                width=250,
            ),
        ],
        spacing=5,
    )
    
    signin_button = ft.Container(
        content=ft.Text(
            "Sign in",
            color=ft.Colors.BLACK87,
            size=16,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.center,
        width=250,
        height=45,
        border_radius=25,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#56CCF2", "#2F80ED"],
        ),
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(0, 3)
        )
    )
    
    or_divider = ft.Row(
        controls=[
            ft.Container(
                width=110,      
                height=1,        
                bgcolor=ft.Colors.BLACK,
                opacity=0.6,
            ),
            ft.Text("or", color=ft.Colors.BLACK, size=13),
            ft.Container(
                width=110,
                height=1,
                bgcolor=ft.Colors.BLACK,
                opacity=0.6,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10, 
    )
    
    google_button = ft.ElevatedButton(
        content=ft.CircleAvatar(
            content=ft.Image(
                src="assets/images/gg.png",
                width=24,
            ),
            bgcolor=ft.Colors.RED
        ),
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=0,
            shadow_color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
        ),
    )

    facebook_button = ft.ElevatedButton(
        content=ft.CircleAvatar(
            content=ft.Image(
                src="assets/images/f.png",
                width=30,
            ),
            bgcolor=ft.Colors.BLUE
        ),
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=0,
            shadow_color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
        ),
    )

    text_new_account = ft.Text(
        "New to Bus Booking?",
        weight=ft.FontWeight.W_600,
        size=12
    )
    
    create_account = ft.TextButton(
        text="Create an account",
        style=ft.ButtonStyle(
            color=ft.Colors.LIGHT_BLUE_900,
            padding=0,
            text_style=ft.TextStyle(
                size=12,
                weight=ft.FontWeight.W_600
            )
        ),
    )


    # --- Layout ---
    layout = ft.Column(
        controls=[
            bus_image,
            ft.Text(
                "Sign In", 
                size=26, 
                weight=ft.FontWeight.BOLD, 
                color="#102542",
            ),
            input_user,
            input_password,
            signin_button,
            or_divider,
            ft.Row(
                controls=[
                    google_button,
                    facebook_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Row(
                controls=[
                    text_new_account,
                    create_account
                ],
                width=250,
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        spacing=5,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        opacity=0.95
    )

    # --- Trang chính ---
    page.add(
        ft.Container(
            content=layout,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors = [
                    "#DFF2EB",
                    "#B9E5E8",
                    "#7AB2D3",
                    "#4A628A"
                ]
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    )

