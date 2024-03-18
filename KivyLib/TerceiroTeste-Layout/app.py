# Importa a biblioteca random para gerar cores aleatórias
import random

# Importa a classe App do módulo kivy.app
from kivy.app import App

# Importa a classe Button do módulo kivy.uix.button
from kivy.uix.button import Button

# Importa a classe BoxLayout do módulo kivy.uix.boxlayout
from kivy.uix.boxlayout import BoxLayout

# Define as cores que serão usadas nos botões
red = [1,0,0,1] # Vermelho
green = [0,1,0,1]  # Verde
blue = [0,0,0,1]  # Azul
purle = [1,0,1,1]  # Roxo

# Define a classe HBoxLayoutExample, que herda da classe App
class HBoxLayoutExample(App):
    
    # Define o método build(), que é chamado automaticamente quando o aplicativo é iniciado
    def build(self):
        # Cria um objeto BoxLayout com um padding de 10 pixels
        layout = BoxLayout(padding=10)
        
        # Cria uma lista de cores
        colors = [red, green, blue, purle]
        
        # Loop que itera 5 vezes
        for i in range(5):
            # Cria um objeto Button com o texto "Este é o botão #i+1" e uma cor de fundo aleatória
            btn = Button(text=f"Este é o botão #{i+1}", 
                         background_color=random.choice(colors))
            
            # Adiciona o botão ao layout
            layout.add_widget(btn)
        # Retorna o objeto layout para ser exibido na tela
        return layout

# Define a cláusula if __name__ == "__main__":, que é usada para garantir que o código dentro dela seja executado apenas quando o arquivo main.py for executado diretamente e não quando for importado como um módulo em outro arquivo
if __name__ == "__main__":
    # Cria uma instância da classe HBoxLayoutExample e chama o método run() para iniciar o loop de eventos do aplicativo
    HBoxLayoutExample().run()
