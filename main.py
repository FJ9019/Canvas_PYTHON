from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.graphics import Ellipse
from kivy.metrics import dp
from kivy.clock import Clock

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
        Clock.schedule_interval(self.my_anim, 1/30)

    def my_anim(self, dt):
        xp, yp = self.ball.pos
        x, y = self.ball.size

        if yp+y+self.vy >= self.height:
            self.vy = -self.vy
        if yp+self.vy <= 0:
            self.vy = -self.vy

        self.ball.pos = (xp, yp+self.vy);    
        pass
    pass

class MainApp(App):
    pass

app = MainApp()
app.run()