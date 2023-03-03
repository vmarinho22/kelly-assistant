import time

import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4') # Open Multilingual WordNet (opcional)

from src import Assistant, NaturalLanguageProcessing, online

assistant = Assistant()
naturalLang = NaturalLanguageProcessing()

def main():

    command = ''
    assistant.speak('init')
    
    while assistant.shutdown_command not in command.lower():
        
        while not online():
            assistant.speak('internet-connection-error')
            time.sleep(5)
        try:
            audio_transpiled = assistant.listen('Ouvindo...')
            
            if assistant.is_called(audio_transpiled):
                assistant.speak('help')
                
                command = assistant.listen('Aguardando comando...')
                
                assistant.speak('running-command')
                time.sleep(1)
                
                keywords = naturalLang.get_keywords(command)
                
                all_synonyms = []
                
                print(keywords)
                
                for keyword in keywords:
                    print(naturalLang.is_similar(keyword, 'horas'))
                    # all_synonyms.append(naturalLang.get_synonyms(keyword))
                
                print(keywords)
                print(all_synonyms)
                
                print('')
                print("Comando: "+ command)
                print('')
            else:
                print('Ignorando comando\n')
                print('')
        except Exception as error: 
            print('Não consigo entender o que falou :/')
            print(error)
            
    assistant.speak('bye')
            
if __name__ == '__main__':
    main()