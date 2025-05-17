# Chatbot Gemini no Google Colab

Este é um chatbot desenvolvido no Google Colab que utiliza o modelo Gemini do Google para interações em linguagem natural. O código configura um ambiente de chat onde o usuário pode inserir mensagens e receber respostas do modelo Gemini.

## Funcionalidades

* **Chat interativo:** Permite uma conversa em tempo real com o chatbot Gemini.
* **Configuração do modelo:** Utiliza o modelo Gemini para gerar respostas contextuais.
* **Leitura de instruções do sistema:** Carrega as instruções do sistema a partir de um arquivo no Google Drive.
* **Utilização do Google Colab:** O código foi desenvolvido para ser executado no ambiente Google Colab, aproveitando seus recursos e bibliotecas.

## Como funciona

1.  **Importação de bibliotecas:**
    * `os`: Para manipulação de variáveis de ambiente.
    * `google.colab.userdata`: Para acessar dados do usuário no Colab.
    * `google.colab.drive`: Para acessar arquivos no Google Drive.
    * `pandas`: Embora importado, não é utilizado no código fornecido.
    * `google.generativeai`: Para interagir com a API do Gemini.
    * `google.genai.types`: Para definir tipos de dados usados na configuração do modelo.

2.  **Configuração do modelo:**
    * `MODELO = "gemini-2.0-flash"`: Define o modelo Gemini a ser utilizado.

3.  **Funções:**
    * `get_api_key_from_gcolab(key_name="GOOGLE_API_KEY")`: Busca a chave da API do Gemini nas variáveis de ambiente do Google Colab.
    * `ler_texto_arquivo_google_drive(file_name)`: Monta o Google Drive e lê o conteúdo de um arquivo de texto.

4.  **Fluxo principal:**
    * Obtém a chave da API do Gemini.
    * Lê as instruções do sistema do arquivo "chat_config.md" no Google Drive.
    * Configura o modelo Gemini com as instruções do sistema.
    * Inicia um loop infinito para interagir com o usuário:
        * Recebe a mensagem do usuário.
        * Envia a mensagem para o modelo Gemini e recebe a resposta.
        * Imprime a resposta do modelo.
        * Encerra o loop quando o usuário digita "Obrigado, seu pedido está sendo preparado".

## Pré-requisitos

* Uma conta do Google.
* Um arquivo "chat_config.md" no Google Drive contendo as instruções do sistema para o chatbot.
* Chave da API do Gemini configurada como uma variável de ambiente no Google Colab.

## Como usar

1.  Abra o código no Google Colab.
2.  Certifique-se de que o arquivo "chat_config.md" esteja no caminho especificado no código.
3.  Execute as células do código no Colab.
4.  Interaja com o chatbot através do terminal do Colab.
