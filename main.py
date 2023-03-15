import time

import nltk

from src import Assistant, Command, online
from src.db import create_tables

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('tagsets')
nltk.download('omw-1.4')  # Open Multilingual WordNet (opcional)


assistant = Assistant()
command = Command()


def main():
    create_tables()

    command_text = ''
    assistant.speak('init')

    while assistant.shutdown_command not in command_text.lower():

        while not online():
            assistant.speak('internet-connection-error')
            time.sleep(5)
        try:
            audio_transpiled = assistant.listen('Ouvindo...')

            if assistant.is_called(audio_transpiled):
                assistant.speak('help')

                command_text = assistant.listen('Aguardando comando...')

                assistant.speak('running-command')
                time.sleep(1)

                command.process(command_text)
            else:
                print('Ignorando comando\n')
                print('')
        except Exception as error:
            print('Não consigo entender o que falou :/')
            print(error)

    assistant.speak('bye')


if __name__ == '__main__':
    main()
