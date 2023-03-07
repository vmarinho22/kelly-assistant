# Kelly Assistant

Uma assistente virtual em pequena escala estilo "Google Assistant¨, "Siri" e "Alexa".

Esse projeto será meu TCC, no qual pretendo implementar sistemas de busca por voz, controle de dispositivos físicos e muito mais!

## Bibliotecas utilizadas

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para transcrição de audio em texto
- [PyAudio](https://pypi.org/project/PyAudio/) - Para manipulação de áudio/dispositivos de áudio
- [gTTS](https://pypi.org/project/gTTS/) - Para geração de audio para resposta
- [Playsound](https://pypi.org/project/playsound/) - Para reproduzir a voz da AI
- [NLTK](https://www.nltk.org/) - Para processamento de linguagem natural
- [OpenAi](https://platform.openai.com/docs/introduction/overview) - Para perguntas a inteligência GPT-3 da OpenAI



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env (que podem ser encontradas no arquivo `.env.example`)

`OPENAI_SECRET_KEY`

`OPENAI_ORGANIZATION_ID`


## Rodando localmente

Para rodar o projeto, você deve ter o Python 3.10+ instalado em sua maquina! Para verificar se o Python está instalado e qual é a versão instalada, use o comando `python -V`.

Primeiramente, clone o projeto.

```bash
  git clone git@github.com:vmarinho22/kelly-assistant.git
```

Entre no diretório do projeto.

```bash
  cd kelly-assistant
```

Instale o pipenv (O [pipenv](https://pipenv.pypa.io/en/latest/) é um gerenciador de dependências do Python).

```bash
  pip install pipenv
```

Após a instalação do pipenv, inicie o ambiente virtual do mesmo.

```bash
  pipenv shell
```

Então, instale as dependências do projeto.

```bash
  pipenv install --all
```

Por fim, execute o arquivo `main.py`.

```bash
  python main.py
```

Pronto! Agora a Kelly Assistant está rodando e escutando seus comandos!

## Comandos suportados

| Comando   | Descrição       | Exemplo de voz                          |
| :---------- | :--------- | :---------------------------------- |
| `hora` | Comando voltado para receber o horário atual | "Que horas são?"
| `data` | Comando voltado para receber a data atual | "Que dia é hoje?"
| `*` | Caso não seja encontrado nenhum acima, a AI irá perguntar a API da OpenAI e trará a resposta (similar ao ChatGPT) | "Por que os pássaros voam?"


Novos comandos serão adicionados ao decorrer do desenvolvimento desse projeto(inclusive, caso tenha sugestões, mande em uma issue ou PR 😊 )

## Autores

- [@vmarinho22](https://github.com/vmarinho22)
- [@DarknessChains](https://github.com/DarknessChains)