import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]= GOOGLE_API_KEY


def voice_input():
    r =sr.Recognizer() # SpeechRecogition happens with the Recognizer class

    with sr.Microphone() as source:
        print("listening...")
        audio= r.listen(source)

        # here we are listenting something
        # next we are to collect this audio inform of text

    try:
        text= r.recognize_google(audio)
        print("you said:", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")


def llm_model_object(user_text):
    model="gemini-1.5-flash"

    model =genai.GenerativeModel(model)

    response = model.generate_content(user_text)
    
    result= response.text

    return result


