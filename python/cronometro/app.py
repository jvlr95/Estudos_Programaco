# Cronômetro em Python
# 
# Importamos os módulos os e time para limpar a tela e adiar a execução do programa,
# respectivamente.
import os
import time

# Criamos a classe Cronometro com os seguintes métodos:
class Cronometro:
    # O método __init__ é o construtor da classe e inicializa as variáveis
    # segundos, minutos e horas com os valores passados como parâmetros.
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    # O método __repr__ é um método mágico que retorna uma representação em string
    # do objeto, neste caso, a formatação da hora, minuto e segundo.
    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    # O método incremento incrementa o valor de segundos em 1, se segundos for igual
    # a 60, ele é zerado e minutos é incrementado em 1, se minutos for igual a 60,
    # ele é zerado e horas é incrementado em 1.
    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        return self

    # O método start inicia a contagem do cronômetro. Ele limpa a tela a cada iteração,
    # imprime a mensagem"Iniciando contagem" seguida da representação em string do
    # objeto self e incrementa o valor de segundos duas vezes com um intervalo de 1
    # segundo entre cada incremento, usando o método time.sleep(1). O loop é interrompido
    # quando o usuário pressiona Ctrl+C, gerando uma exceção KeyboardInterrupt.
    def start(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Iniciando contagem --> " + str(self) + " <--")
                self.incremento().incremento()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nContagem interrompida pelo usuário.")

# Criamos uma instância da classe Cronometro com os valores iniciais de horas,
# minutos e segundos zerados.
cronometro1 = Cronometro(0)

# Chamamos o método start da instância cronometro1 para iniciar a contagem.
cronometro1.start()
