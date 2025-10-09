import time

import pandas as pd
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def run_progress_bar(records: int):
    print(records)
    progress_bar = st.progress(0, text="Working...")

    for i in range(records + 1):
        progress_bar.progress(i / records, text=f"Processing record {i}/{records}")
        time.sleep(1)  # Simulate work being done
    st.success("Done!")


def read_file(uploaded_file: UploadedFile):
    st.write("File uploaded successfully!")
    df = pd.read_excel(uploaded_file)
    st.write("DataFrame:")
    st.dataframe(df)


st.write("Hello, Streamlit!")

with st.form("upload_form"):
    uploaded_file = st.file_uploader("Choose a file")
    records = st.number_input("Number of records to process", min_value=1)

    submit_button = st.form_submit_button("Submit")

    if submit_button and uploaded_file is not None:
        read_file(uploaded_file)
    elif submit_button and records:
        run_progress_bar(records)
