import os
import pytube
from moviepy.editor import *
import time
from dialog import exibir_caixa_dialogo_info, exibir_caixa_dialogo_erro, obter_input_caixa_dialogo

# Função para obter o caminho da pasta "Downloads"
def obter_caminho_downloads():
    if os.name == 'nt':  # Windows
        downloads_folder = os.path.expanduser("~\\Downloads")
    else:  # Outros sistemas operacionais
        downloads_folder = os.path.expanduser("~/Downloads")
    return downloads_folder

# Função para baixar o vídeo do YouTube
def baixar_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    nome_arquivo = video.download('./')
    return nome_arquivo

# Função para converter o vídeo para o formato WAV
def converter_para_wav(nome_arquivo):
    video = VideoFileClip(nome_arquivo)
    nome_saida = os.path.join(obter_caminho_downloads(), os.path.basename(nome_arquivo).replace('.mp4', '.wav'))
    video.audio.write_audiofile(nome_saida, codec='pcm_s16le')
    video.close()  # Fechar o vídeo após a conversão
    return nome_saida

# Função para excluir o arquivo MP4
def excluir_arquivo(nome_arquivo):
    time.sleep(6)  # Atraso de 6 segundos
    try:
        os.remove(nome_arquivo)
        exibir_caixa_dialogo_info("O arquivo foi excluído com sucesso!")
    except OSError as e:
        exibir_caixa_dialogo_erro(f"Ocorreu um erro ao excluir o arquivo: {e}")

# Prompt para baixar e converter o vídeo
url = obter_input_caixa_dialogo("Digite a URL do vídeo do YouTube:")
nome_arquivo = baixar_video(url)
nome_saida = converter_para_wav(nome_arquivo)
excluir_arquivo(nome_arquivo)

exibir_caixa_dialogo_info("A conversão para WAV foi concluída!")
