from flet import *
from flet import colors, icons


def main(page: Page):
    page.title = "Button Types"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.appbar = AppBar(
        bgcolor="#034582",
        color="#ffffff",
        center_title=True,
        title=Text(value="Button Types")
    )

    page.add(
        Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                ElevatedButton(text="Elevated Button", bgcolor=colors.AMBER, color=colors.WHITE, height=35, width=200),
                FilledButton(text="Filled Button", icon=icons.APPS),
                FilledButton(text="Filled Button", icon=icons.APPS, disabled=True),
                IconButton(icon=icons.SMART_BUTTON, icon_color=colors.INDIGO),
                IconButton(icon=icons.SMART_BUTTON, icon_color=colors.INDIGO, disabled=True),
                OutlinedButton(text="Outline Button"),
                OutlinedButton(text="Outline Button", disabled=True),
            ]
        )
    )


flet.app(target=main)
