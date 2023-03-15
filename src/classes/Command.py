import json
import os
import time
from datetime import datetime

import openai
from dotenv import load_dotenv

from .Assistant import Assistant
from .AudioSystem import AudioSystem
from .NaturalLanguageProcessing import NaturalLanguageProcessing
from .Event import Event

load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
openai.api_key = os.getenv("OPENAI_SECRET_KEY")


class Command:
    """
        Dedicated class to process commands of assistant
    """
    natura_lang = NaturalLanguageProcessing()
    commands = {}
    assistant = Assistant()
    audio_system = AudioSystem()
    event = Event()
    current_command_tokens = []

    def __init__(self) -> None:
        abspath = os.path.abspath("src/files/commands_synonyms.json")

        with open(abspath, encoding='utf-8') as commands_file:
            parsed_json = json.load(commands_file)
            self.commands = parsed_json

    def find_command(self, keywords: list[str]) -> str:
        """
            Method to find an internal command
        """
        for keyword in keywords:
            for key in self.commands:
                if keyword in self.commands[key]:
                    return key

        return ''

    def try_find_command_by_synonyms(self, keywords: list[str]) -> str:
        """
            Method to try to find internal command using synonyms of keywords
        """
        for keyword in keywords:
            synonyms = self.natura_lang.get_synonyms(keyword)

            internal_command = self.find_command(synonyms)

            if internal_command != '':
                return internal_command

        return ''

    def run_command(self, command_key: str) -> None:
        """
            Method to run command
        """
        command = ''
        output_text = ''

        match command_key:
            case "hora":
                command = 'hora'
                now = datetime.now()
                hour = now.hour
                minutes = now.minute
                hour_text = f'hora{hour > 1 and "s" or ""}'
                minutes_text = f'minuto{minutes > 1 and "s" or ""}'

                output_text = f'O horário atual é {hour} {hour_text} e {minutes} {minutes_text}'

            case "data":
                command = 'data'
                now = datetime.now()
                day = now.day
                month = self.event.full_month[now.month - 1]
                year = now.year

                output_text = f'A data atual é dia {day} de {month} de{year}'

        self.assistant.speak('command-output', output_text)
        self.audio_system.delete_audio('command-output')

        print(f'Comando "{command}" executando')

    def process(self, command: str) -> bool:
        """
            Method to process and run command
        """

        print('')
        print("Comando: " + command)
        print('')

        keywords = self.natura_lang.get_keywords(command)

        print(keywords)

        self.current_command_tokens = keywords

        internal_command = self.find_command(keywords)

        print("internal command "+internal_command)

        # try to find internal command using synonyms of keywords
        if internal_command == '':
            internal_command = self.try_find_command_by_synonyms(keywords)

        if internal_command != '':
            self.run_command(internal_command)
            return True

        # If command has not found, the AI transform command in question and use OPENAI API to search the answer

        response = openai.Completion.create(model="text-davinci-003", prompt=command, temperature=0, max_tokens=2048)

        final_openai_text_response = response["choices"][0]["text"]

        self.assistant.speak('command-output', final_openai_text_response)
        self.audio_system.delete_audio('command-output')
        
        return True
