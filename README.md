# Chico Assistente - Assistente Virtual de Voz

A aplicação é um assistente de voz feito em python, para automatizar funcionalidades que auxiliam os condutores de veículos, como ligar/desligar motor, faróis, ar-condicionado, etc.

## Funcionalidades:

O assistente atende a alguns comandos de voz, tais como:

1. Ligar/Desligar motor.
2. Abrir porta/Travar portas.
3. Ligar/Desligar faróis.
4. Ligar/Desligar o ar-condicionado.
5. Abrir/Fechar janela.

## Configuração

Para utilizar a aplicação, é necessário ter o Python 3.7.9 e o Node.JS instalado em seu computador. Além disso, é preciso instalar as seguintes dependências:

- nltk
- SpeechRecognition
- pyaudio

Para instalar as dependências, execute o seguinte comando no terminal:

```
pip install -r requirements.txt
```

## Como utilizar

Para utilizar o Chico Assistente, execute o seguinte arquivo no terminal: `chico.py`.

```
config.json --> Treinamento do assistente para os possíveis comandos de voz (OBS_01)
chico.py --> Arquivo principal do backend do programa
executor.py --> Arquivo de testes registrados com biblioteca unittest
```

**OBS 01**: 

Certifique-se de que o assistente está treinado. Isso pode ser verificado através da presença de um arquivo `db.sqlite3` dentre os arquivos nos diretórios. Caso não exista esse arquivo, deve-se treinar o voicebot para obter as informações. Isso pode ser feito através do arquivo `chico.py`.

## Configuração de comandos

As mensagens estão configurados no arquivo *config*. Para adicionar novos comandos, basta adicionar uma nova entrada ao arquivo, seguindo o seguinte formato:

```
 "nome": "chico",
  "acoes": [
      {
          "nome": "ligar",
          "objetos": [
              "motor",
              "farol",
              "ar"
          ]
      },
      ...
```



