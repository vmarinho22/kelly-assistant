# Kelly Assistant

Uma assistente virtual em pequena escala estilo "Google Assistant¨, "Siri" e "Alexa".

Esse projeto será meu TCC, no qual pretendo implementar sistemas de busca por voz, controle de dispositivos físicos e muito mais!

Até o momento, esse sistema consegue reconhecer as palavras ditas no microfone e as transcreve em texto bruto.

## Bibliotecas utilizadas

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para transcrição de audio em texto
- [PyAudio](https://pypi.org/project/PyAudio/) - Para manipulação de áudio/dispositivos de áudio 


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