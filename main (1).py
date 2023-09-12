import datetime
import webbrowser
import pyttsx3
import wikipedia
import pyjokes
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from PIL import Image, ImageTk
import tkinter as tk
import random
import threading

global engine


def gui(con, text):
    global root

    def sd():
        label.destroy()

    if con == 1:

        label = tk.Label(root, text='')
        label.config(text=text)
        root.after(5000, sd)
        label.pack()
    elif con == 0:

        global abc
        global from_color
        global to_color
        # Create a tkinter window
        root = tk.Tk()
        label = tk.Label(root,
                         text='                        Hello there, this is Ava, your own Personal Assistant!!!                       ',
                         bg="white", pady=20)
        label.pack()
        # Load the image
        image = Image.open(r"C:\Users\shiva\Documents\tp.jpg")
        image = image.resize((400, 400), Image.Resampling.LANCZOS)
        # Create a tkinter canvas
        canvas = tk.Canvas(root, width=image.width, height=image.height)
        canvas.pack()

        # Convert the image to a tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)

        # Create a canvas image from the tkinter-compatible image
        canvas_image = canvas.create_image(0, 0, anchor='nw', image=tk_image)

        from_color = (72, 217, 116)

        to_color = (
            random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))  # Random color    # Red
        canvas.itemconfig(canvas_image, image=tk_image)
        from_color, to_color = from_color, to_color

        abc = canvas.create_polygon(180, 162,
                                    214, 161,
                                    214, 164,
                                    207, 164,
                                    203, 167,
                                    203, 172,
                                    190, 172,
                                    182, 169,
                                    180, 166,
                                    180, 162
                                    , fill='#5E0403')

        canvas.delete(abc)

        def change_color():
            global is_changing
            if is_changing:

                global abc
                canvas.delete(abc)
                global from_color
                global to_color
                if (random.randint(0, 500) % 3 != 0):
                    abc = canvas.create_polygon(180, 162,
                                                214, 161,
                                                214, 164,
                                                207, 164,
                                                203, 167,
                                                203, 172,
                                                190, 172,
                                                182, 169,
                                                180, 166,
                                                180, 162
                                                , fill='#5E0403')
                else:
                    None

                to_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Loop through each pixel in the image
                for x in range(image.width):
                    for y in range(image.height):
                        # Get the color of the current pixel
                        color = image.getpixel((x, y))

                        # Check if the color matches the color you want to change
                        if color == from_color:
                            # If it matches, change it to the new color
                            image.putpixel((x, y), to_color)
                global tk_image
                tk_image = ImageTk.PhotoImage(image)
                canvas.itemconfig(canvas_image, image=tk_image)
                from_color, to_color = to_color, from_color
                root.after(200, change_color)

        def toggle_changing():
            global is_changing
            is_changing = not is_changing
            if is_changing:
                change_color()

        def bind_lis():
            threadA = threading.Thread(target=toggle_changing)
            threadB = threading.Thread(target=listen)
            threadA.start()
            threadB.start()

        # def stop_lis():

        global is_changing
        is_changing = False
        button = tk.Button(root, text="Start/Stop", bg="black", fg="white", command=bind_lis)
        button.pack(pady=20)
        button.pack()

        # Start the tkinter event loop

        root.mainloop()


def translator1():
    flag = 0

    # A tuple containing all the language and
    # codes of the language will be detected

    dic = ('afrikaans', 'af', 'albanian', 'sq',
           'amharic', 'am', 'arabic', 'ar',
           'armenian', 'hy', 'azerbaijani', 'az',
           'basque', 'eu', 'belarusian', 'be',
           'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
           'bg', 'catalan', 'ca', 'cebuano',
           'ceb', 'chichewa', 'ny', 'chinese (simplified)',
           'zh-cn', 'chinese (traditional)',
           'zh-tw', 'corsican', 'co', 'croatian', 'hr',
           'czech', 'cs', 'danish', 'da', 'dutch',
           'nl', 'english', 'en', 'esperanto', 'eo',
           'estonian', 'et', 'filipino', 'tl', 'finnish',
           'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
           'gl', 'georgian', 'ka', 'german',
           'de', 'greek', 'el', 'gujarati', 'gu',
           'haitian creole', 'ht', 'hausa', 'ha',
           'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
           'hi', 'hmong', 'hmn', 'hungarian',
           'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
           'id', 'irish', 'ga', 'italian',
           'it', 'japanese', 'ja', 'javanese', 'jw',
           'kannada', 'kn', 'kazakh', 'kk', 'khmer',
           'km', 'korean', 'ko', 'kurdish (kurmanji)',
           'ku', 'kyrgyz', 'ky', 'lao', 'lo',
           'latin', 'la', 'latvian', 'lv', 'lithuanian',
           'lt', 'luxembourgish', 'lb',
           'macedonian', 'mk', 'malagasy', 'mg', 'malay',
           'ms', 'malayalam', 'ml', 'maltese',
           'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
           'mn', 'myanmar (burmese)', 'my',
           'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
           'pashto', 'ps', 'persian', 'fa',
           'polish', 'pl', 'portuguese', 'pt', 'punjabi',
           'pa', 'romanian', 'ro', 'russian',
           'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
           'serbian', 'sr', 'sesotho', 'st',
           'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
           'slovak', 'sk', 'slovenian', 'sl',
           'somali', 'so', 'spanish', 'es', 'sundanese',
           'su', 'swahili', 'sw', 'swedish',
           'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
           'te', 'thai', 'th', 'turkish',
           'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
           'ug', 'uzbek', 'uz',
           'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
           'yiddish', 'yi', 'yoruba',
           'yo', 'zulu', 'zu')

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            gui(1, "listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            gui(1, "Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            gui(1, f"The User said {query}\n")
        except Exception as e:
            gui(1, "say that again please.....")
            return "None"
        return query

    # Input from user
    # Make input to lowercase
    query = takecommand()
    while (query == "None"):
        query = takecommand()

    def destination_language():
        gui(1, "Enter the language in which you want to convert.")
        gui(1, "")


        to_lang = takecommand()
        while (to_lang == "None"):
            to_lang = takecommand()
        to_lang = to_lang.lower()
        return to_lang

    to_lang = destination_language()

    # Mapping it with the code
    while (to_lang not in dic):
        gui(1, "Language in which you are trying\
                to convert is currently not available ,\
                please input some other language")
        gui(1, "")
        to_lang = destination_language()

    to_lang = dic[dic.index(to_lang) + 1]

    # invoking Translator
    translator = Translator()

    # Translating from src to dest
    text_to_translate = translator.translate(query, dest=to_lang)

    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow=False)

    # Using save() method to save the translated
    # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")

    # Using OS module to run the translated voice.
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Define function to listen for voice command
def listen():
    global is_changing
    if is_changing:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            gui(1, "Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            gui(1, "Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            gui(1, f"User said: {query}\n")
        except sr.UnknownValueError:
            gui(1, "Unable to recognize speech.")
            return "None"
        except sr.RequestError as e:
            gui(1, f"Request error: {e}")
            speak("Sorry, unable to access the speech recognition service at the moment.")
            return "None"

        print(query)
        query = query.lower()
        if 'translator' in query:
            speak('translator opened')
            translator1()
        elif 'google' in query:
            website = query.split('google')[1]
            url = f"https://www.google.com/search?q={website}"
            webbrowser.open(url)
            speak(f"seaching {website} for you.")
        elif 'open' in query:
            website = query.split(" ")[-1]
            url = f"https://www.{website}.com"
            webbrowser.open(url)
            speak(f"Opening {website} for you.")
        elif 'search' in query:
            search_query = query.split(" ")[-1]
            try:
                speak(f"Searching for {search_query} on Wikipedia.")
                result = wikipedia.summary(search_query, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                gui(1, f"Disambiguation error: {e}")
                speak("Sorry, please be more specific.")
            except wikipedia.exceptions.PageError as e:
                gui(1, f"Page error: {e}")
                speak("Sorry, unable to find any results for that search query.")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")

            speak(f"The current time is {time}.")
        elif 'exit' in query:
            speak("Goodbye!")
        elif 'how are you' in query:
            # Define a list of possible responses
            responses = [
                "I'm doing well, thank you for asking.",
                "I'm functioning properly, thank you.",
                "I'm feeling a little tired, but overall I'm doing okay.",
                "I don't have feelings, but I'm functioning as intended.",
                "I'm a chatbot, so I don't have emotions like humans do, but I'm ready to assist you.",
                "Thanks for asking, I'm programmed to help you with your needs, so let's get started!",
                "I'm doing fantastic, ready to assist you with anything you need!",
                "Hi, I feel good, thanks for asking",
                "I'm always ready to help you, so I'm doing great!",
                "I'm a computer program, so I don't have feelings, but I'm here to help you!",
            ]

            # Generate a random response from the list
            random_response = random.choice(responses)
            speak(random_response)
            print(random_response)
        else:
            speak("Sorry, I didn't understand that. Can you please repeat your command?")

def main():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")


if __name__ == '__main__':
    thread1 = threading.Thread(target=gui, args=(0, ""))
    thread2 = threading.Thread(target=main)
    thread2.start()
    thread1.start()
    thread2.join()
    thread1.join()
    engine.stop()
