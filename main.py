import time

import nltk

from src import Assistant, Command, online

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('tagsets')
nltk.download('omw-1.4')  # Open Multilingual WordNet (opcional)


assistant = Assistant()
command = Command()


def main():

    command_text = ''
    assistant.speak('init')

    while assistant.shutdown_command not in command_text.lower():

        while not online():
            assistant.speak('internet-connection-error')
            time.sleep(5)
        try:

            # assistant.speak('help')
            raw_command_text = assistant.listen('Ouvindo...')
            
            print('raw_command_text', raw_command_text)

            if assistant.is_called(raw_command_text):
                
                command_text = assistant.removeAssistantNameOfCommand(raw_command_text)

                assistant.speak('running-command')
                time.sleep(1)

                command.process(command_text)
            else:
                print('Assistente não chamada\n')
                print('')
        except Exception as error:
            print('Não consigo entender o que falou :/')
            print(error)

    assistant.speak('bye')


if __name__ == '__main__':
    main()
