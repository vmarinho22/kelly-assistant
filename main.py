import time

from src import AudioSystem, SpeechRecognition, online

speech_recognition = SpeechRecognition()
audio_system = AudioSystem()

def main():

    command = ''
    audio_system.play_audio('init')
    
    while 'desligar assistente' not in command.lower():
        
        while not online():
            audio_system.play_audio('internet-connection-error')
            time.sleep(5)
    
        audio_data = speech_recognition.listen('Ouvindo...')
        
        try:
            audio_transpiled = speech_recognition.transpile_audio(audio_data)
            
            if 'kelly' in audio_transpiled.lower():
                audio_system.play_audio('help')
                audio_command_data = speech_recognition.listen('Aguardando comando')
                
                command = speech_recognition.transpile_audio(audio_command_data)
                
                audio_system.play_audio('running-command')
                time.sleep(1)
                
                print('')
                print("Comando: "+ command)
                print('')
            else:
                print('Ignorando comando\n')
                print('')
        except: 
            print('Não consigo entender o que falou :/')
            
    audio_system.play_audio('bye')
            
if __name__ == '__main__':
    main()