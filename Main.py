import PySimpleGUI

class TelaPython:
    def __init__(self):
        PySimpleGUI.theme('BlueMono')
        layout = [
            [PySimpleGUI.Text('Nome',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='nome')],
            [PySimpleGUI.Text('Rua',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='rua')],
            [PySimpleGUI.Text('Bairro',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='bairro')],
            [PySimpleGUI.Text('Numero',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='nmr')],
            
            [PySimpleGUI.Text('Lanches',size=(10,0))],
            [PySimpleGUI.Radio('X-Bacon','lanche',key='bacon'),PySimpleGUI.Radio('X-Salada','lanche',key='salada')],
            [PySimpleGUI.Radio('X-Filé    ','lanche' ,key='file'),PySimpleGUI.Radio('X-Picanha','lanche',key='picanha')],

            #[PySimpleGUI.Text('Adcionais',size=(10,0))],
            #[PySimpleGUI.Checkbox('Bacon       ','Adcionais',key='add_bacon'),PySimpleGUI.Checkbox('Bata Frita média','Adcionais',key='add_bt_media')],
            #[PySimpleGUI.Checkbox('Cheedar    ','Adcionais' ,key='add_cheedar'),PySimpleGUI.Checkbox('Bata Frita grande','Adcionais',key='add_bt_grande')],

            [PySimpleGUI.Text('Refrigerantes',size=(30,0)),],
            [PySimpleGUI.Radio('Coca-Cola','refri',key='coca'),PySimpleGUI.Radio('Fanta','refri',key='fanta')],
            [PySimpleGUI.Radio('Guaraná   ','refri',key='guarana'),PySimpleGUI.Radio('Vazio','refri',key='vazio')],

            [PySimpleGUI.Text('Opção Refrigerante',size=(30,0)),],
            [PySimpleGUI.Radio('Lata','op', key='lata'), PySimpleGUI.Radio('Garrafa 2 Litros', 'op', key='garrafa')],

            [PySimpleGUI.Text('Quantidade de Lanches',size=(30,0))],
            #[PySimpleGUI.Slider(range=(1,50),default_value=1,orientation='h',size=(15,15),key='lanches')],
            [PySimpleGUI.Input(size=(5,0),key='lanches')],
            [PySimpleGUI.Text('Quantidade de Refrigerantes',size=(30,0))],
            #[PySimpleGUI.Slider(range=(1,50),default_value=1,orientation='h',size=(15,15),key='refri')],
            [PySimpleGUI.Input(size=(5,0),key='refri')],
            
            [PySimpleGUI.Text('Observação',size=(10,0))],
            [PySimpleGUI.Input(size=(30,5),key='obs')],
            [PySimpleGUI.Button('Enviar pedido ', key='envPedido')],
            [PySimpleGUI.Text('Desenvolvido por Murilo Martins                                    Versão: 2.16.4' , size=(60,0))]
        ]
        self.janela = PySimpleGUI.Window("Lanchonete Lanches").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = str(self.values['nome'])
            rua = self.values['rua']
            bairro = self.values['bairro']
            numero = int(self.values['nmr'])
            xBacon = self.values['bacon']
            xFile = self.values['file']
            xSalada = self.values['salada']
            xPicanha = self.values['picanha']
            #addbacon = self.values['add_bacon']
            #addcheedar = self.values['add_cheedar']
            #addbtmedia = self.values['add_bt_media']
            #addbtgrande = self.values['add_bt_grande']
            coca = self.values['coca']
            fanta = self.values['fanta']
            guarana = self.values['guarana']
            vazio = self.values['vazio']
            sliderLanches = int(self.values['lanches'])
            sliderRefri = int(self.values['refri'])
            obs = self.values['obs']
            lata = self.values['lata']
            garrafa = self.values['garrafa']

            if sliderLanches == 0:
                print("########### NOTA DE ERRO !!! ##########")
                print("########### NOTA DE ERRO !!! ##########")
                print("########### NOTA DE ERRO !!! ##########")
                print("########### NOTA DE ERRO !!! ##########")
                exit()

            if xBacon == True:
                lanches = 'X-Bacon'
            if xFile == True:
                lanches = 'X-Filé'
            if xSalada == True:
                lanches = 'X-Salada'
            if xPicanha == True:
                lanches = 'X-Picanha'
            
            if lata == True:
                escolha = "Lata"
            if garrafa == True:
                escolha = "Garrafa 2L"

            if coca == True:
                refrigerante = 'Coca-Cola'
            if fanta == True:
                refrigerante = 'Fanta'
            if guarana == True:
                refrigerante = 'Guaraná'
            if vazio == True:
                refrigerante = 'Nenhum'
                sliderRefri = 0
                escolha = 'Nenhum'

            print('########### NOTA DE PEDIDO ##########')
            print(f'Nome: {nome}')
            print(f'Rua: {rua}')
            print(f'Bairro: {bairro}')
            print(f'Numero: {numero}')
            print(f'Lanches: {lanches}')
            #print(f'Adcionais: {adcionais}')
            print(f'Refrigerantes: {refrigerante}')
            print(f'Opção: {escolha}')
            print(f'Quantidade de Lanches: {sliderLanches}')
            print(f'Quantidade de Refri: {sliderRefri}')
            print(f'Observação: {obs}')
            print('#####################################')

tela = TelaPython()
tela.Iniciar()    