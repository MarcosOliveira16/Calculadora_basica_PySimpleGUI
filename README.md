# Calculadora basica PySimpleGUI
Projeto de calculadora básica utilizando da biblioteca do PySimplieGUI e vídeos do youtube.


# Calculadora Básica com PySimpleGUI

Este script cria uma calculadora básica utilizando a biblioteca PySimpleGUI, que oferece uma maneira simples de criar interfaces gráficas em Python. A calculadora possui um visor, botões numéricos, operações aritméticas básicas, e funcionalidades de reinício e apagar. Além disso, inclui um menu com opções de salvar e sair, além de informações sobre o programa.

## Instalação

### Instalação do PySimpleGUI
Para executar este script, você precisa instalar a biblioteca PySimpleGUI. Isto pode ser feito utilizando o seguinte comando:
```bash
pip install PySimpleGUI
```

## Código da Calculadora

### Importação da Biblioteca e Definição do Tema
```python
import PySimpleGUI as sg

sg.theme('BlueMono')
```

### Configuração da Janela e Layout
Definimos o tamanho da janela e criamos o layout da interface, incluindo o menu e os botões.

```python
# tamanho da tela
WIN_W = 30  # largura em caracteres
WIN_H = 50  # altura em caracteres

menu_layout = [
    ['File', ['Save', 'Exit']],
    ['Tools', ['Waiting']],
    ['Help', ['About']]
]

# elementos da nossa tela - linha 1
layout = [
    [sg.Menu(menu_layout)],
    [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='visor'),  # visor
     sg.Button('<-', font=('Consolas', 20), key='apagar'),  # botão de apagar
     sg.Button('c', font=('Consolas', 20), key='reiniciar')],  # botão de resetar
    # linha 2
    [sg.Button('7', font=('Consolas', 20), key='sete'),
     sg.Button('8', font=('Consolas', 20), key='oito'),
     sg.Button('9', font=('Consolas', 20), key='nove'),
     sg.Button('+', font=('Consolas', 20), key='adicao'),
     sg.Button('x', font=('Consolas', 20), key='multiplicacao')],
    # linha 3
    [sg.Button('4', font=('Consolas', 20), key='quatro'),
     sg.Button('5', font=('Consolas', 20), key='cinco'),
     sg.Button('6', font=('Consolas', 20), key='seis'),
     sg.Button('-', font=('Consolas', 20), key='subtracao'),
     sg.Button('/', font=('Consolas', 20), key='divisao')],
    # linha 4
    [sg.Button('1', font=('Consolas', 20), key='um'),
     sg.Button('2', font=('Consolas', 20), key='dois'),
     sg.Button('3', font=('Consolas', 20), key='tres'),
     sg.Button('0', font=('Consolas', 20), key='zero'),
     sg.Button('=', font=('Consolas', 20), key='igual')]
]
```

### Classe da Aplicação
Criamos a classe `App` que gerencia a lógica da calculadora.

```python
class App():
    def __init__(self):
        self.janela = sg.Window('Calculadora Basica', layout=layout, margins=(
            0, 0), resizable=True, return_keyboard_events=False)
        self.resultado = 0
        self.operacao = ''
        self.janela.read(timeout=1)  # taxa de atualização na tela do app

    def about(self):
        sg.popup('About', 'Github: MarcosOliveira16')

    def result(self):
        if self.operacao == '+':
            return float(self.resultado) + float(self.valores['visor'])
        if self.operacao == '-':
            return float(self.resultado) - float(self.valores['visor'])
        if self.operacao == 'x':
            return float(self.resultado) * float(self.valores['visor'])
        if self.operacao == '/':
            return float(self.resultado) / float(self.valores['visor'])

    def comecar(self):
        while True:
            eventos, self.valores = self.janela.read()

            if eventos in (None, 'Exit', sg.WINDOW_CLOSED):
                break

            if eventos in ('About'):
                self.about()

            if eventos in ('um'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='1')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '1')

            if eventos in ('dois'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='2')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '2')

            if eventos in ('tres'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='3')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '3')

            if eventos in ('quatro'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='4')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '4')

            if eventos in ('cinco'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='5')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '5')

            if eventos in ('seis'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='6')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '6')

            if eventos in ('sete'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='7')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '7')

            if eventos in ('oito'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='8')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '8')

            if eventos in ('nove'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='9')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '9')

            if eventos in ('zero'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='0')
                else:
                    self.janela['visor'].update(value=self.valores['visor'] + '0')

            if eventos in ('reiniciar'):
                self.resultado = 0
                self.janela['visor'].update(value=self.resultado)

            if eventos in ('apagar'):
                self.janela['visor'].update(value=self.valores['visor'][:-1])

            if eventos in ('adicao'):
                if self.operacao != '':
                    self.resultado = self.result()
                else:
                    self.operacao = '+'
                    self.resultado = self.valores['visor']
                self.janela['visor'].update(value='')

            if eventos in ('subtracao'):
                if self.operacao != '':
                    self.resultado = self.result()
                else:
                    self.operacao = '-'
                    self.resultado = self.valores['visor']
                self.janela['visor'].update(value='')

            if eventos in ('divisao'):
                if self.operacao != '':
                    self.resultado = self.result()
                else:
                    self.operacao = '/'
                    self.resultado = self.valores['visor']
                self.janela['visor'].update(value='')

            if eventos in ('multiplicacao'):
                if self.operacao != '':
                    self.resultado = self.result()
                else:
                    self.operacao = 'x'
                    self.resultado = self.valores['visor']
                self.janela['visor'].update(value='')

            if eventos in ('igual'):
                self.resultado = self.result()
                self.janela['visor'].update(value=self.resultado)
                self.resultado = 0
                self.operacao = ''
```

### Execução da Aplicação
Criamos uma instância da classe `App` e chamamos o método `comecar` para iniciar a aplicação.

```python
App().comecar()
```

### Descrição dos Componentes e Funcionalidades

- **Menu**: O menu inclui opções de `Save`, `Exit`, `Waiting` e `About`. A opção `About` exibe um popup com informações sobre o autor.
- **Visor**: Exibe o valor atual e resultados das operações.
- **Botões Numéricos**: Botões de `0` a `9` para entrada de números.
- **Operações**: Botões para `+`, `-`, `x`, `/`, para operações de adição, subtração, multiplicação e divisão, respectivamente.
- **Funções Especiais**:
  - `Apagar`: Apaga o último dígito inserido.
  - `Re

iniciar`: Reinicia o visor e o valor de resultado.
  - `Igual`: Calcula e exibe o resultado da operação atual.

Este código é uma implementação completa de uma calculadora básica com uma interface gráfica amigável, utilizando PySimpleGUI.
