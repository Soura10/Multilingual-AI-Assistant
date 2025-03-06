import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me anything"):
        with st.spinner("Listening..."): # the spinner is ratating
            text=voice_input()
            response=llm_model_object(text)
            text_to_speech(response)


            audio_file= open("speech.mp3","rb")  # voice input passing in form of voice file
            audio_bytes= audio_file.read()



            st.text_area()
            st.audio()
            st.download_button()


if __name__=="__main__":
    try:
        main()
    except Exception as e:
        raise e    
                



            