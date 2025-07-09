import streamlit as st
from summarizer import summarize_text

st.title("QuickSummarizer AI ✨")
text_input = st.text_area("Paste your text or article here:")

if st.button("Summarize"):
    if text_input:
        summary = summarize_text(text_input)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter text to summarize.")