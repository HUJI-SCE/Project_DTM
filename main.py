import streamlit as st
import numpy as np


import streamlit as st
import pandas as pd
import tempfile

st.title("Project_DTM_Assaf_and_Ori")

# Upload video file
video_file = st.file_uploader("videos/ori_and_amit_wedding.mp4", type=["mp4"])

if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    # Display the video
    st.video(tfile.name)

# Upload CSV file
csv_file = st.file_uploader("SakerJunctionData_1730.csv", type=["csv"])

if csv_file is not None:
    # Read and display the CSV file
    df = pd.read_csv(csv_file)
    st.write(df)
