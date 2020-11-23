import PySimpleGUI

class TelaPython:
    def __init__(self):
        PySimpleGUI.theme('BlueMono')
        layout = [
            [PySimpleGUI.Text('Seu Nome',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='nome')],
            [PySimpleGUI.Text('Rua',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='rua')],
            [PySimpleGUI.Text('Bairro',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='bairro')],
            [PySimpleGUI.Text('Numero',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='casa')],
            [PySimpleGUI.Text('Lanches',size=(10,0))],
            [PySimpleGUI.Radio('X-Bacon','lanche',key='bacon'),PySimpleGUI.Radio('X-Salada','lanche',key='salada')],
            [PySimpleGUI.Radio('X-Filé    ','lanche' ,key='file'),PySimpleGUI.Radio('X-Picanha','lanche',key='picanha')],
            [PySimpleGUI.Text('Refrigerantes',size=(11,0))],
            [PySimpleGUI.Radio('Coca-Cola','refri',key='coca'),PySimpleGUI.Radio('Fanta','refri',key='fanta')],
            [PySimpleGUI.Radio('Guaraná   ','refri',key='guarana'),PySimpleGUI.Radio('Vazio','refri',key='vazio')],
            [PySimpleGUI.Text('Quantidade de Lanches',size=(30,0))],
            [PySimpleGUI.Slider(range=(1,50),default_value=0,orientation='h',size=(15,15),key='lanches')],
            [PySimpleGUI.Text('Quantidade de Refrigerantes',size=(30,0))],
            [PySimpleGUI.Slider(range=(1,50),default_value=0,orientation='h',size=(15,15),key='refri')],
            [PySimpleGUI.Text('Observação',size=(10,0))],
            [PySimpleGUI.Input(size=(30,5),key='obs')],
            [PySimpleGUI.Button('Finalizar pedido '), PySimpleGUI.Button('Cancelar pedido', key='buttonExit')],
            [PySimpleGUI.Text('Desenvolvido por Murilo Martins                                    Versão: 2.16.4' , size=(60,0))]
        ]
        self.janela = PySimpleGUI.Window("Lanchonete Lanches").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = str(self.values['nome'])
            rua = self.values['rua']
            bairro = self.values['bairro']
            numero = int(self.values['casa'])
            xBacon = self.values['bacon']
            xFile = self.values['file']
            xSalada = self.values['salada']
            xPicanha = self.values['picanha']
            coca = self.values['coca']
            fanta = self.values['fanta']
            guarana = self.values['guarana']
            vazio = self.values['vazio']
            sliderLanches = self.values['lanches']
            sliderRefri = self.values['refri']
            obs = self.values['obs']
            button = self.values['buttonExit']

            if button == True:
                exit()     
            if xBacon == True:
                lanches = 'X-Bacon'
            if xFile == True:
                lanches = 'X-Filé'
            if xSalada == True:
                lanches = 'X-Salada'
            if xPicanha == True:
                lanches = 'X-Picanha'

            if coca == True:
                refrigerante = 'Coca-Cola'
            if fanta == True:
                refrigerante = 'Fanta'
            if guarana == True:
                refrigerante = 'Guaraná'
            if vazio == True:
                refrigerante = 'Nenhum'
                sliderRefri = 0

            print('########### NOTA DE PEDIDO ##########')
            print(f'Nome: {nome}')
            print(f'Rua: {rua}')
            print(f'Bairro: {bairro}')
            print(f'Numero: {numero}')
            print(f'Lanches: {lanches}')
            print(f'Refrigerantes: {refrigerante}')
            print(f'Quantidade de Lanches: {sliderLanches}')
            print(f'Quantidade de Refri: {sliderRefri}')
            print(f'Observação: {obs}')
            print('#####################################')

tela = TelaPython()
tela.Iniciar()    