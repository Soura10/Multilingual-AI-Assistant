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



            st.text_area(label="Response",value=response,height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download speech",
                               data=audio_bytes, 
                               file_name="speech.mp3",
                               mime="audio/mp3")


if __name__=="__main__":
    try:
        main()
    except Exception as e:
        raise e    
                



            