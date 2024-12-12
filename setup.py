from setuptools import find_packages,setup


setup(
    name = "multilingual assistant",
    version= "0.0.1",
    author = "Souradeep",
    author_email="souradeeproy.10@gmail.com",
    packages=find_packages(),
    install_requirements = ["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai", "python-dotenv", "streamlit"]
    
)