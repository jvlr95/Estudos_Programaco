# Importa a classe App do módulo kivy.app
from kivy.app import App

# Importa a classe Label do módulo kivy.uix.label
from kivy.uix.label import Label

# Define a classe MainApp, que herda da classe App
class MainApp(App):
    
    # Define o método build(), que é chamado automaticamente quando o aplicativo é iniciado
    def build(self):
        # Cria um objeto Label com o texto "Fala galera!", tamanho relativo de (.5, .5) e posição relativa centralizada usando pos_hint
        label = Label(text='Fala galera!', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        # Retorna o objeto Label para ser exibido na tela
        return label

# Define a cláusula if __name__ == "__main__":, que é usada para garantir que o código dentro dela seja executado apenas quando o arquivo app.py for executado diretamente e não quando for importado como um módulo em outro arquivo
if __name__ == "__main__":
    # Cria uma instância da classe MainApp e chama o método run() para iniciar o loop de eventos do aplicativo
    app = MainApp()
    app.run()
