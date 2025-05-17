# Chatbot para Atendimento em Restaurante no Google Colab

Este projeto implementa um chatbot utilizando o modelo de linguagem Gemini do Google, executado no ambiente Google Colab. O chatbot foi desenvolvido para atuar como um atendente online de restaurante, interagindo com usuários em linguagem natural para fornecer informações e auxiliar em tarefas relacionadas ao estabelecimento.

## Visão Geral

O objetivo principal deste projeto é demonstrar a utilização do modelo Gemini para criar um sistema de conversação interativo especificamente para um restaurante. O código configura um ambiente de chat onde os usuários podem inserir mensagens e receber respostas geradas pelo modelo Gemini. A configuração do sistema, incluindo as instruções iniciais para o modelo, é carregada de um arquivo externo (`chat_config.md`) no Google Drive, permitindo fácil personalização do comportamento do chatbot para atender às necessidades específicas de um restaurante.

## Funcionalidades

* **Chat Interativo:** Permite conversas em tempo real com o chatbot Gemini. Os usuários podem inserir mensagens de texto e receber respostas contextuais geradas pelo modelo.
* **Modelo de Linguagem Gemini:** Utiliza o modelo de linguagem Gemini do Google para gerar respostas. O Gemini é capaz de compreender e gerar linguagem natural, permitindo interações mais ricas e complexas.
* **Atendimento ao Cliente de Restaurante:** O chatbot foi projetado para auxiliar clientes de um restaurante, podendo fornecer informações sobre o cardápio, horários de funcionamento, localização, reservas e outras dúvidas frequentes.
* **Configuração do Sistema:** As instruções iniciais para o modelo Gemini são carregadas de um arquivo externo (`chat_config.md`) no Google Drive. Isso permite personalizar o comportamento do chatbot para atender às necessidades específicas de um restaurante, como saudações personalizadas, informações sobre pratos específicos e procedimentos de reserva.
* **Execução no Google Colab:** O projeto foi desenvolvido para ser executado no Google Colab.

## Como Funciona

O código é estruturado em torno de algumas funções principais:

1.  **Importação de Bibliotecas:**

    * `os`: Para manipulação de variáveis de ambiente, como a chave da API do Gemini.
    * `google.colab.userdata`: Para acessar dados do usuário armazenados no Google Colab.
    * `google.colab.drive`: Para montar e acessar arquivos no Google Drive.
    * `pandas`: Embora importado, não seja utilizado no código fornecido.
    * `google.generativeai`: Para interagir com a API do Gemini.
    * `google.genai.types`: Para definir tipos de dados usados na configuração do modelo.
2.  **Configuração do Modelo:**

    * `MODELO = "gemini-2.0-flash"`: Define o modelo Gemini a ser utilizado.
3.  **Funções:**

    * `get_api_key_from_gcolab(key_name="GOOGLE_API_KEY")`: Esta função busca a chave da API do Gemini armazenada como uma variável de ambiente no Google Colab.
    * `ler_texto_arquivo_google_drive(file_name)`: Esta função monta o Google Drive e lê o conteúdo de um arquivo de texto. O arquivo contém as instruções do sistema para o Gemini.
4.  **Fluxo Principal:**

    1.  **Obtém a Chave da API:** A chave da API do Gemini é obtida usando a função `get_api_key_from_gcolab()`.
    2.  **Lê as Instruções do Sistema:** As instruções do sistema para o Gemini são lidas do arquivo `chat_config.md` no Google Drive usando a função `ler_texto_arquivo_google_drive()`.
    3.  **Configura o Modelo:** O modelo Gemini é configurado com as instruções do sistema lidas do arquivo.
    4.  **Inicia o Loop de Chat:** O código entra em um loop infinito onde:

        * Recebe a mensagem do usuário através do terminal do Colab.
        * Envia a mensagem para o modelo Gemini e recebe a resposta gerada.
        * Imprime a resposta do modelo no terminal.
        * O loop se encerra quando o usuário digita a mensagem de encerramento.
## Detalhes Técnicos

### Arquivo de Configuração (`chat_config.md`)

O arquivo `chat_config.md` contém as instruções do sistema que guiam o comportamento do chatbot. Este arquivo deve estar localizado no Google Drive e conter formatação Markdown. Ele deve ser adaptado para incluir informações relevantes para o contexto de um restaurante, como:

* Saudações personalizadas para o restaurante.
* Informações sobre o cardápio, incluindo descrição dos pratos, preços e ingredientes.
* Horário de funcionamento do restaurante.
* Informações de contato e localização.
* Procedimentos para reservas.
* Respostas para perguntas frequentes dos clientes.

### Chave da API do Gemini

Para que o código funcione corretamente, você precisa obter uma chave de API do Gemini e configurá-la como uma variável de ambiente no Google Colab.

## Pré-requisitos

* Uma conta do Google.
* Acesso ao Google Colab.
* Um arquivo `chat_config.md` no Google Drive contendo as instruções do sistema para o chatbot, adaptado para o contexto de um restaurante.
* Chave da API do Gemini configurada como uma variável de ambiente no Google Colab.

## Como Usar

1.  Abra o código no Google Colab.
2.  Verifique se o arquivo `chat_config.md` está localizado no caminho correto no seu Google Drive e contém as informações relevantes para o restaurante.
3.  Execute as células do código no Colab.
4.  Interaja com o chatbot através do terminal do Colab.
