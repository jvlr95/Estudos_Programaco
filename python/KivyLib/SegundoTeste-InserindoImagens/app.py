# Importa a classe App do módulo kivy.app
from kivy.app import App

# Importa a classe AsyncImage do módulo kivy.uix.image
from kivy.uix.image import AsyncImage

# Define a classe MainApp, que herda da classe App
class MainApp(App):
    
    # Define o método build(), que é chamado automaticamente quando o aplicativo é iniciado
    def build(self):
        # Cria um objeto AsyncImage com a imagem em https://supermariorun.com/assets/img/stage/mario03.png,
        # tamanho relativo de (1, .5) e posição relativa centralizada usando pos_hint
        img = AsyncImage(source="https://supermariorun.com/assets/img/stage/mario03.png",
                       size_hint=(1, .5), pos_hint={'center_x': .5, 'center_y': .5})
        # Retorna o objeto AsyncImage para ser exibido na tela
        return img

# Define a cláusula if __name__ == "__main__":, que é usada para garantir que o código dentro dela seja executado apenas quando o arquivo main.py for executado diretamente e não quando for importado como um módulo em outro arquivo
if __name__ == "__main__":
    # Cria uma instância da classe MainApp e chama o método run() para iniciar o loop de eventos do aplicativo
    app = MainApp()
    app.run()
