
# Kelly Assistant

Um assistente virtual em pequena escala estilo "Google Assistant¨, "Siri" e "Alexa".

Esse projeto será meu TCC, onde pretendo implementar sistemas de busca por voz, controle de dispositivos criados e muito mais!

Até o momento esse sistema consegue reconhecer as palavras ditas no microfone, e os transcrevem em texto bruto.
## Bibliotecas utilizadas

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para transcrição de audio em texto
- [PyAudio](https://pypi.org/project/PyAudio/) - Para manipulação de aúdio/dispositivos de aúdio 


## Rodando localmente

Para rodar o projeto, você deve ter o Python 3+ instalado em sua maquina! Para verificar a se o Python está instalado e a versão instalada, use o comando `python -V`.

Clone o projeto

```bash
  git clone git@github.com:vmarinho22/kelly-assistant.git
```

Entre no diretório do projeto

```bash
  cd kelly-assistant
```

Instale o pipenv (O [pipenv](https://pipenv.pypa.io/en/latest/) é um gerenciador de dependências do Python)

```bash
  pip install pipenv
```

Após a instalação, inicie o ambiente virtual do pipenv

```bash
  pipenv shell
```

Então, instale as dependências do projeto

```bash
  pipenv install --all
```

Por fim, execute o arquivo `main.py`

```bash
  python main.py
```

Pronto! Agora o Kelly Assistant está rodando e escutando seus comandos!
