from re import MULTILINE
from typing_extensions import ReadOnly
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextIpunt

class MainApp(App):
    def build(self):
        self.operator = [ "/", "*", "+", "-"]
        self.lastWasOperator = None
        self.lastButton = None
        mainLayout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(
                multiline = False, readonly = True, halign = "right", font_size = 55
                )
        mainLayout.add_widget(self.solution)
        buttons = [
                ["7", "8", "9", "/"]
                ["4", "5", "6", "*"]
                ["1", "2", "3", "-"]
                [".", "0", "C", "+"]
                ]
        for row in buttons:
            hLayout = BoxLayout()
            for label in row:
                button = Button(
                        text = label,
                        posHint={'center_x': 0.5, 'ceenter_y': 0.5}.
                )
                button.bind(onPress=self.onButtonPress)
                hLayout.add_widget(button)
            mainLayout.add_widget(hLayout)
            equalsButton.bind(onPress=self.onSolution)
            mainLayout.add_widget(equalsButton)

            return mainLayout
