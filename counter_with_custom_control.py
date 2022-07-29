from flet import *


class CustomButton(UserControl):
    def __init__(self, label, onClick):
        super().__init__()
        self.label = label
        self.onClick = onClick

    def build(self):
        return ElevatedButton(text=self.label, on_click=self.onClick,bgcolor="#763483",color="#ffffff")


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
                CustomButton(label="-", onClick=decrement),
                textField,
                CustomButton(label="+", onClick=increment),
            ]
        )
    )


flet.app(target=main)
