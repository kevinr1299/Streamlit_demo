import pandas as pd
import streamlit as st


st.write("Hello, Streamlit!")

with st.form("upload_form"):
    uploaded_file = st.file_uploader("Choose a file")
    submit_button = st.form_submit_button("Submit")

    if submit_button and uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("DataFrame:")
        st.dataframe(df)
