from flet import *


def main(page: Page):
    page.title = "Counter App"
    page.vertical_alignment = "center"
    page.appbar = AppBar(
        bgcolor="#034582",
        color="#ffffff",
        center_title=True,
        title=Text(value="Counter App")
    )

    textField = TextField(value="0", width=100)

    def increment(e):
        textField.value = int(textField.value) + 1
        page.update()

    def decrement(e):
        textField.value = int(textField.value) - 1
        page.update()

    page.add(
        Row(
            alignment="center",
            controls=[
                ElevatedButton(text="-", on_click=decrement),
                textField,
                ElevatedButton(text="+", on_click=increment),
            ]
        )
    )


flet.app(target=main)
