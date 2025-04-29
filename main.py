from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.graphics import Ellipse
from kivy.metrics import dp

class MainWidget(Widget):
    pass

class CanvasTest(Widget):
    pass

class AnimationBall(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vy = dp(5)
        with self.canvas:
            self.ball = Ellipse(pos=(dp(350), 0), size=(dp(50), dp(50)))
    pass

class MainApp(App):
    pass

app = MainApp()
app.run()