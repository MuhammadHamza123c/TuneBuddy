import streamlit as st
import pandas as pd
import numpy as np
from check import get_poster
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

simiar_path=os.path.join(script_dir, "similar.npy")
data_path=os.path.join(script_dir,"song_data.csv")

data = pd.read_csv(data_path)
similar = np.load(simiar_path)

songs_title = data['song'].tolist()
songs_title.insert(0, "Select a song")

st.markdown(
    """
    <h1 style='text-align: center; font-family: "Helvetica, Arial, sans-serif"; color: #1E90FF;'>
        TuneBuddy 🎵
    </h1>
    <p style='text-align: center; font-size:18px; color: #888888;'>
        Discover songs you’ll love based on your favorites!
    </p>
    """,
    unsafe_allow_html=True
)

selected_song = st.selectbox("Choose a song:", songs_title)

if selected_song != "Select a song":
    try:
        song_index = data[data['song'] == selected_song].index[0]
        similarities = similar[song_index]
        indexed_arr = list(enumerate(similarities))
        sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1], reverse=True)
        top_indices = [index for index, value in sorted_indexed_arr[:4]]

        for idx in range(0, 4, 2):
            if idx + 1 < len(top_indices):
                col1, spacer, col2 = st.columns([1, 0.1, 1])
                with col1:
                    st.markdown("<br><br><br>", unsafe_allow_html=True)
                    i = top_indices[idx]
                    poster_url = get_poster(data['song'].iloc[i])
                    st.image(poster_url, use_container_width=True)
                    st.subheader(data['song'].iloc[i])
                    st.write("Artist:", data['artist'].iloc[i])
                with col2:
                    st.markdown("<br><br><br>", unsafe_allow_html=True)
                    i = top_indices[idx + 1]
                    poster_url = get_poster(data['song'].iloc[i])
                    st.image(poster_url, use_container_width=True)
                    st.subheader(data['song'].iloc[i])
                    st.write("Artist:", data['artist'].iloc[i])
        st.markdown("<br><br>", unsafe_allow_html=True)

    except IndexError:
        st.write("Song is not available!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Hamza</p>", unsafe_allow_html=True)
