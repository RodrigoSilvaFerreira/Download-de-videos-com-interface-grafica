import PySimpleGUI as sg
from video import download_video
from threading import Thread

#Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Digite o novo nome do video que irá baixar.')],
    [sg.Input(key='nome')],
    [sg.Text(key='nome_vazio')],
    [sg.Text('Digite ou cole a url do video que gostaria de baixar.')],
    [sg.Input(key='url')],
    [sg.Text(key='texto')],
    [sg.Button('Baixar Video',key='baixar'), sg.Button('Sair',key='sair')],
    [sg.Output(size=(45,8))]
]

# Janela
janela = sg.Window('Download de Videos do youtube', layout=layout)

# Eventos e valores
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'baixar':
        if values['nome'] == '':
            janela['nome_vazio'].update('Por favor, escreva um nome para o arquivo')
        elif values['url'] == '':
            janela['texto'].update('Preencha o campo com uma url')
        else:
            thread_arquivo = Thread(target=download_video, args=(values['url'], values['nome']), daemon=True)
            thread_arquivo.start()
            janela['url'].update('')
            janela['nome'].update('')
    elif event == 'sair':
        break