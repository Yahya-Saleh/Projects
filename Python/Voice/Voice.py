import speech_recognition
import re
from time import sleep
from sys import exit

recognizer = speech_recognition.Recognizer()

def main():
    while True:
        with speech_recognition.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)

        words = recognizer.recognize_google(audio)

        # Respond to speech
        if "hello" in words:
            print("Hello to you too!")
            name()
        elif "how are you" in words:
            print("I am well, thanks!")
            name()
        elif "goodbye" in words:
            print("Goodbye to you too!")
            exit(0)
        else:
            print("huh?")
            print()
            sleep(1)

def name():
    sleep(1)
    print()
    with speech_recognition.Microphone() as source:
        print("Your name is...")
        audio = recognizer.listen(source)

    words = recognizer.recognize_google(audio)

    matches = re.search("my name is (.*)", words)
    if matches:
        print(f"Hey, {matches[1]}.")
    else:
        print("Hey, you.")

if __name__ == "__main__":
    main()