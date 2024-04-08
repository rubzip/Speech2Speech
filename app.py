import streamlit as st
import librosa, librosa.display
from Audio import Audio
from settings import WAVE_OUTPUT_FILE, DURATION


def main():
    audio = Audio(DURATION, WAVE_OUTPUT_FILE)
    
    title = "Speech 2 Speech Model"
    st.title(title)

    if st.button("Record"):
        with st.spinner(f'Recording for {4} seconds ....'):
            audio.record()
    
    if st.button('Play'):
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except:
            st.write("Please record sound first")

main()