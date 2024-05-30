import streamlit as st
from pydub import AudioSegment
import streamlit.components.v1 as components

# Function to play audio
def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# Set the title of the app
st.title("Chinese traditional instrument")

# Display instrument images and play sound on click
instruments = {
    "Guqin": ("guqin.jpg", "guqin.mp3"),
    "Erhu": ("erhu.jpg", "erhu.mp3"),
    # "Violin": ("violin.jpg", "violin.mp3")
}

for instrument, (img_path, audio_path) in instruments.items():
    st.subheader(instrument)
    if st.button(f"Play {instrument} sound"):
        play_audio(audio_path)
    st.image(img_path, use_column_width=True)
    st.markdown("---")

# Run the app with streamlit
# Save this script as app.py and run `streamlit run app.py` in your terminal
