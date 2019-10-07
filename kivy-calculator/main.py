from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class ErrorIndicatorWidget(FloatLayout):
    pass


class CalcWidget(BoxLayout):
    visor = ObjectProperty(None)
    calc_on_error = False
    error_led = NumericProperty(0)

    def button_press(self, button):
        if button.text == 'CE':
            self.visor.text = ''
            self.calc_on_error = False
            self.error_led = 0

        elif button.text == 'Enter' and not self.calc_on_error==True :
            try:
                self.visor.text = str(eval(self.visor.text))
            except:
                self.visor.text = "ERROR"
                self.calc_on_error = True
                self.error_led = 1

        elif not self.calc_on_error:
            self.visor.text = self.visor.text + button.text


class CalcApp(App):
    def build(self):
        return CalcWidget()


if __name__ == '__main__':
    CalcApp().run()
