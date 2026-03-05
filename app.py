import streamlit as st
from transcript import get_transcript
from summarizer import summarize_text

st.set_page_config(page_title="YouTube Video Summarizer")

st.title("YouTube Video Summarizer")
st.write("Paste a YouTube link and get a summary.")

url = st.text_input("Enter YouTube URL")

if st.button("Summarize"):
    if not url:
        st.error("Please enter a URL")
    else:
        with st.spinner("Fetching transcript..."):
            transcript = get_transcript(url)

        if not transcript:
            st.error("Could not retrieve transcript")
        else:
            with st.spinner("Generating summary..."):
                summary = summarize_text(transcript)

            st.subheader("Summary")
            st.write(summary)