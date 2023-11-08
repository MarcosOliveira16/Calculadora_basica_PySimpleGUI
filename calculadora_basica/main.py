import PySimpleGUI as sg

sg.theme('BlueMono')

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


class App():
    def __init__(self):
        self.janela = sg.Window('Calculadora basica', layout=layout, margins=(
            0, 0), resizable=True, return_keyboard_events=False)  # 'resizable' para poder diminuir e aumentar a tela do app, 'return_keybords' para não retornar nada digitado no terminal
        self.resultado = 0
        self.operacao = ''
        self.janela.read(timeout=1)  # taxa de atualização na tela do app
        """for item in range(1, 5):  # de 1 a 5 pq são cinco botões por linha
            for botao in layout[item]:
                botao.expand(expand_x=True, expnad_y=True)"""

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

            # fechando o app
            if eventos in (None, 'Exit', sg.WINDOW_CLOSED):
                break

            if eventos in ('About'):
                self.about()

            if eventos in ('um'):
                # se valor atual for '0', atualizar para '1'
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='1')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '1')  # se valor atual não for '0', concatenar com o valor '1'

            if eventos in ('dois'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='2')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '2')

            if eventos in ('tres'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='3')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '3')

            if eventos in ('quatro'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='4')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '4')

            if eventos in ('cinco'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='5')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '5')

            if eventos in ('seis'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='6')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '6')

            if eventos in ('sete'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='7')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '7')

            if eventos in ('oito'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='8')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '8')

            if eventos in ('nove'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='9')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '9')

            if eventos in ('zero'):
                if self.valores['visor'] == '0':
                    self.janela['visor'].update(value='0')
                else:
                    self.janela['visor'].update(
                        value=self.valores['visor'] + '0')

            # reiniciando o visor e resultado
            if eventos in ('reiniciar'):
                self.resultado = 0
                self.janela['visor'].update(value=self.resultado)

            # apagando o valor atual
            if eventos in ('apagar'):
                self.janela['visor'].update(value=self.valores['visor'][:-1])

            # funções para tirar os numeros do visor e fazer a operação chamando o 'result'
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


App().comecar()
