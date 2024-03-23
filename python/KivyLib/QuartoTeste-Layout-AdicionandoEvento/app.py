#-------------------------------------------------------------------------------------------------#
# Importa a classe App do módulo kivy.app
# from kivy.app import App
# Importa a classe Button do módulo kivy.uix.button
# from kivy.uix.button import Button

# class MainApp(App):
#     def build(self):
#         button = Button(text='SALVE!!!',
#                         size_hint=(.5, .5),
#                         pos_hint={'center_x': .5, 'center_y': .5})
#         button.bind(on_press=self.onPressButton)
#         return button

#     def onPressButton(self, instance):
#         print('Você apertou o botão! êêêêêêêêêêê')

# if __name__ == '__main__':
#     MainApp().run()
#-------------------------------------------------------------------------------------------------#

# O kivy também fornece uma linguagem chamada de KV.
# Principio da separação de interesses e faz parte do padrão da arquitetura Model-View-Controller

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def onPressButton(self):
        print('Você apertou o botão!')

if __name__ == '__main__':
    ButtonApp().run()
