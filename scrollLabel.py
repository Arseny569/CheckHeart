# Модуль с классом-наследником ScrollView для создания инструкции, у которой при необходимости включается полоса прокрутки
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
# Здесь должен быть твой код
class ScrollLabel(ScrollView):
    def __init__(self, ltext, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(
        text=ltext,
        markup=True,
        size_hint_y=None,
        font_size='18sp',
        halign='left',
        valign='top'
        )

        self.add_widget(self.label)

        self.label.bind(size=self.resize)

    def resize(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]