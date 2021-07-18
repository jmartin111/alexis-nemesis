#! /bin/bash

# some shitty code to play with stt / tts

import os
import speech_recognition as sr
import subprocess


def command():
    shell_command = "ls -la".split(' ')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bob: Listening...")
        audio=r.listen(source, timeout=2000, phrase_time_limit=2000)
        #TODO: use factory functions to implement this
        try:
            query = r.recognize_google(audio)
            if query == "test":
                print(f"calling: {shell_command}")
                subprocess.call(shell_command)
            return query
        except subprocess.SubprocessError as spe:
            print(spe)

command()
print("done")
