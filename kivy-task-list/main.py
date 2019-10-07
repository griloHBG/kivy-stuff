from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class TaskWidget(BoxLayout):
    _colorDict = {"Low": (.2, 1, .2, 1), "Medium": (1, 1, .2, 1), "High": (1, .2, .2, 1), '': (.2, .3, .4, 1)}
    priority_color = ListProperty((.2, .3, .4, 1))
    task = ObjectProperty(None)
    when = ObjectProperty(None)
    priority = ObjectProperty(None)

    def change_priority(self, text):
        print(text)
        self.priority_color = self._colorDict[self.priority.text]
        print(self.priority.text)

    def remove_task(self):
        self.parent.remove_widget(self)

    def check_box_change(self):
        if self.done.active:
            self.task.disabled = True
            self.when.disabled = True
            self.priority.disabled = True
        else:
            self.task.disabled = False
            self.when.disabled = False
            self.priority.disabled = False


class TaskManagerLayout(BoxLayout):
    pass


class ScreenLayout(BoxLayout):
    task_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ScreenLayout, self).__init__(**kwargs)
        self.task_manager.bind(minimum_height=self.task_manager.setter('height'))

    def add_task(self):
        self.task_manager.add_widget(TaskWidget())


class TaskApp(App):
    def build(self):
        return ScreenLayout()


if __name__ == '__main__':
    app = TaskApp()
    app.run()
