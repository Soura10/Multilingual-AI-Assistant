import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE API KEY")
os.environ["GOOGLE_API_KEY"]= GOOGLE_API_KEY


def voice_input():
    pass



def text_to_speech():
    pass


def llm_model_object():
    pass

