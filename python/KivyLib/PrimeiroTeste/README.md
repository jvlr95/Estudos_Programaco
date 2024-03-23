# Instalação do Python 3.12.0 e Kivy

## Instalação do asdf-vm

Acesse o site [https://asdf-vm.com/guide/getting-started.html] e siga as instruções para instalar o asdf-vm.

## Instalação do Python 3.12.0

1. Adicione o plugin do Python ao asdf:

    ```bash
    asdf plugin-add python
    ```

2. Instale o Python 3.12.0:

    ```bash
    asdf install python 3.12.0
    ```

3. Defina globalmente o Python 3.12.0:

    ```bash
    asdf global python 3.12.0
    ```

## Instalação do Kivy

1. Instale o Kivy usando o pip:

    ```bash
    pip install kivy
    ```

2. Verifique se o Kivy foi instalado corretamente:

    ```bash
    python -m pip list | grep Kivy
    ```

    Você deve ver a saída `kivy 2.3.0`.

## Testando a aplicação

1. Navegue até a pasta do projeto no terminal ou prompt de comando.

2. Execute o seguinte comando para iniciar o aplicativo Kivy:

    ```bash
    python3 app.py
    ```

    Isso iniciará o aplicativo Kivy com o rótulo "Fala galera!" no centro da tela.

