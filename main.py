from src import SpeechRecognition


def main():
    speech_recognition = SpeechRecognition()
    command = ''
    
    while 'desligar assistente' not in command.lower():
        audio_data = speech_recognition.listen('Aguardando fala inicial')
        
        try:
            audio_transpiled = speech_recognition.transpile_audio(audio_data)
            
            if 'kelly' in audio_transpiled.lower():
                audio_command_data = speech_recognition.listen('Aguardando comando')
                
                command = speech_recognition.transpile_audio(audio_command_data)
                
                print("Comando: "+ command)
                print('')
            else:
                print('Ignorando comando\n')
                print('')
        except: 
            print('Não consigo entender o que falou :/')
            
if __name__ == '__main__':
    main()