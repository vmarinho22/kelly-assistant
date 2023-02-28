import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while 1 == 1:
        print("Aguardando fala")
        audio_text = recognizer.listen(source)
        print("Time over, thanks")
        
        try:
            audio_transpiled = recognizer.recognize_google(audio_text, language = "pt-BR")
            
            if(audio_transpiled == 'Kelly' or audio_transpiled == 'kelly'):
                print("Aguardando comando")
                audio_command_text = recognizer.listen(source)
                print("Time over, thanks")
                
                audio_command_transpiled = recognizer.recognize_google(audio_command_text, language = "pt-BR")
                
                print("Comando: "+ audio_command_transpiled)
            else:
                print("Text: "+ audio_transpiled)
        except:
            print("Sorry, I did not get that")