import pytube

def download_video(link,nome_arquivo):
    yt = pytube.YouTube(link)
    print('Baixado', link)

    # Mostrar detalhes do video
    print(f'Titulo: {yt.title}')
    print(f'Número de views: {yt.views}')
    print(f'Tamanho do vídeo: {yt.length} segundos')
    print(f'Avaliação do video: {yt.rating}')

    # Usa a maior resolução
    ys = yt.streams.get_highest_resolution()

    # Começa o Donwload do video
    print('Baixando...')
    ys.download(filename=f'{nome_arquivo}.mp4')
    print('Download completo')