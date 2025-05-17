import os
from google.colab import userdata
from google.colab import drive
import pandas as pd
from google import genai
from google.genai import types

MODELO = "gemini-2.0-flash"

def get_api_key_from_gcolab(key_name="GOOGLE_API_KEY"):
    os.environ['GOOGLE_API_KEY'] = userdata.get(key_name)
    if os.environ['GOOGLE_API_KEY'] is None:
        raise ValueError(f"A chave '{key_name}' não foi encontrada nas variáveis de ambiente.")
    return os.environ['GOOGLE_API_KEY']

def ler_texto_arquivo_google_drive(file_name):
    drive.mount('/content/drive')
    file_path = f'/content/drive/My Drive/códigos/ChatBot-Gemini 1.0/{file_name}'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado em: {file_path}.")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

get_api_key_from_gcolab()

chat_config = types.GenerateContentConfig(
    system_instruction=ler_texto_arquivo_google_drive('chat_config.md')
)

cliente = genai.Client()
chat = cliente.chats.create(model=MODELO, config=chat_config)

while True:
    mensagem = input("Digite sua mensagem: ")
    reposta = chat.send_message(mensagem)
    print(reposta.text)
    if mensagem == "Obrigado, seu pedido está sendo preparado":
        break
