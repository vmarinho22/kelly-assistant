import time

from src import Assistant, online

assistant = Assistant()

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
                
                print('')
                print("Comando: "+ command)
                print('')
            else:
                print('Ignorando comando\n')
                print('')
        except: 
            print('Não consigo entender o que falou :/')
            
    assistant.speak('bye')
            
if __name__ == '__main__':
    main()